#!/usr/bin/env python
""" generated source for module Call """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.types.TupleType import TupleType
from pysonarsq.java.types.InstanceType import InstanceType
from pysonarsq.java.types.UnionType import UnionType
from pysonarsq.java.types.DictType import DictType


from java.util import Set
from java.util import List

from Node import Node

from pysonarsq.java.Binding import Binding
ATTRIBUTE = Binding.Kind.ATTRIBUTE
CLASS = Binding.Kind.CLASS
CONSTRUCTOR = Binding.Kind.CONSTRUCTOR
FUNCTION = Binding.Kind.FUNCTION
METHOD = Binding.Kind.METHOD
MODULE = Binding.Kind.MODULE
PARAMETER = Binding.Kind.PARAMETER
SCOPE = Binding.Kind.SCOPE
VARIABLE = Binding.Kind.VARIABLE

class Call(Node):
    """ 
    func = Node()
    args = List()
    keywords = List()
    kwargs = Node()
    starargs = Node()
    """

    def __init__(self, func, args, keywords, kwargs, starargs, start, end):
        super(Call, self).__init__(start, end)
        
        self.func = func
        self.args = args
        self.keywords = keywords
        self.kwargs = kwargs
        self.starargs = starargs
        
        self.addChildren(func, kwargs, starargs)
        self.addChildren(args)
        self.addChildren(keywords)
        

    # 
    #      * Most of the work here is done by the static method invoke, which is also
    #      * used by Analyzer.applyUncalled. By using a static method we avoid building
    #      * a NCall node for those dummy calls.
    #      
    def resolve(self, s):

        # // experiment with isinstance
        #         if (func.isName() && func.asName().id == "isinstance") {
        #             if (len(args) == 2) {
        #                 if (args.get(0).isName()) {
        #                     Type rType = resolveExpr(args.get(1), s);
        #                     s.put(args.get(0).asName().id, args.get(0), rType, SCOPE);
        #                 }
        #             }
        #         }
        
        opType = self.resolveExpr(self.func, s)
        aTypes = self.resolveAndConstructList(self.args, s)
        kwTypes = dict()
        
        for kw in self.keywords:
            kwTypes[kw.getArg()] = self.resolveExpr(kw.getValue(), s)
            
        kwargsType = None if self.kwargs is None else self.resolveExpr(self.kwargs, s)
        starargsType = None if self.starargs is None else self.resolveExpr(self.starargs, s)
        
        if opType.isUnionType():
            from pysonarsq.java.Analyzer import Analyzer
            
            types = opType.asUnionType().getTypes();
            retType = Analyzer.self.builtins.unknown;       
                 
            for funcType in types:
                t = self.resolveCall(funcType, aTypes, kwTypes, kwargsType, starargsType);
                retType = UnionType.union(retType, t)
                
            return retType
        else:
            return self.resolveCall(opType, aTypes, kwTypes, kwargsType, starargsType)

    def resolveCall(self, rator, aTypes, kwTypes, kwargsType, starargsType):
        from pysonarsq.java.Analyzer import Analyzer

        if rator.isFuncType():
            ft = rator.asFuncType();
            return self.apply(ft, aTypes, kwTypes, kwargsType, starargsType, self)
        elif rator.isClassType():
            return InstanceType(rator, self, aTypes)
        else:
            self.addWarning("calling non-function and non-class: " + str(rator))
            return Analyzer.self.builtins.unknown

    @classmethod
    def apply(cls, func, aTypes, kTypes, kwargsType, starargsType, call):
        from pysonarsq.java.Analyzer import Analyzer
        from pysonarsq.java.Scope import Scope
        
        Analyzer.self.removeUncalled(func)
        
        if func.func is not None and not func.func.called:
            Analyzer.self.nCalled += 1
            func.func.called = True
            
        if func.getFunc() is None:
            #  func without definition (possibly builtins)
            return func.getReturnType()
        elif call is not None and Analyzer.self.inStack(call):
            func.setSelfType(None)
            return Analyzer.self.builtins.unknown
            
        if call is not None:
            Analyzer.self.pushStack(call)
            
        argTypeList = list()

        if func.getSelfType() is not None:
            argTypeList.append(func.getSelfType())
        elif func.getCls() is not None:
            argTypeList.append(func.getCls().getCanon())
            
        if aTypes is not None:
            argTypeList += list(aTypes)
            
        cls.bindMethodAttrs(func)
        
        funcTable = Scope(func.getEnv(), Scope.ScopeType.FUNCTION)
        
        if func.getTable().getParent() is not None:
            funcTable.setPath(func.getTable().getParent().extendPath(func.func.name.id))
        else:
            funcTable.setPath(func.func.name.id)
            
        fromType = cls.bindParams(call, funcTable, func.func.args,
                    func.func.vararg, func.func.kwarg,
                    argTypeList, func.defaultTypes, kTypes, kwargsType, starargsType)
                    
        cachedTo = func.getMapping(fromType)
        if cachedTo is not None:
            func.setSelfType(None)
            return cachedTo
        else:
            toType = cls.resolveExpr(func.func.body, funcTable);
            if cls.missingReturn(toType):
                Analyzer.self.putProblem(func.func.name, "Function not always return a value")
                if call is not None:
                    Analyzer.self.putProblem(call, "Call not always return a value")
            
            func.addMapping(fromType, toType)
            func.setSelfType(None)
            return toType

    @classmethod
    def bindParams(cls, call, funcTable, args, fvarargs, fkwargs, aTypes, dTypes, kwTypes, kwargsType, starargsType):
        from pysonarsq.java.Analyzer import Analyzer
        from pysonarsq.java.Binder import Binder        

        fromType = TupleType()
        aSize = 0 if aTypes is None else len(aTypes)
        dSize = 0 if dTypes is None else len(dTypes)
        nPositional = len(args) - dSize
        
        if starargsType is not None and starargsType.isListType():
            starargsType = starargsType.asListType().toTupleType()
            
        j = 0
        for i, arg in enumerate(range(len(args))):
            arg = args[i]
            if i < aSize:
                aType = aTypes[i]
            elif i - nPositional >= 0 and i - nPositional < dSize:
                aType = dTypes[i - nPositional]
            else:
                if kwTypes is not None and args[i].isName() and args[i].asName().id in kwTypes:
                    aType = kwTypes[args[i].asName().id]
                    del kwTypes[args[i].asName().id]
                elif starargsType is not None and starargsType.isTupleType() and j < len(starargsType.asTupleType().getElementTypes()):
                    aType = starargsType.asTupleType().get(j)
                    j += 1
                else:
                    aType = Analyzer.self.builtins.unknown
                    if call is not None:
                        Analyzer.self.putProblem(args[i], "unable to bind argument:" + str(args[i]))
            
            Binder.bind(funcTable, arg, aType, Binding.Kind.PARAMETER)
            fromType.add(aType)

        if fkwargs is not None:
            if kwTypes is not None and len(kwTypes):
                kwValType = UnionType.newUnion(kwTypes.values());
                Binder.bind(funcTable, fkwargs, DictType(Analyzer.self.builtins.BaseStr, kwValType), Binding.Kind.PARAMETER)
            else:
                Binder.bind(funcTable, fkwargs, Analyzer.self.builtins.unknown, Binding.Kind.PARAMETER)
                
        if fvarargs is not None:
            if len(aTypes) > len(args):
                starType = TupleType(aTypes[len(args) : len(aTypes)]);
                Binder.bind(funcTable, fvarargs, starType, Binding.Kind.PARAMETER)
            else:
                Binder.bind(funcTable, fvarargs, Analyzer.self.builtins.unknown, Binding.Kind.PARAMETER)
                
        return fromType

    @classmethod
    def bindMethodAttrs(cls, cl):
        if cl.getTable().getParent() is not None:
            cl_ = cl.getTable().getParent().getType();
            if cl_ is not None and cl_.isClassType():
                cls.addReadOnlyAttr(cl, "im_class", cl_, CLASS)
                cls.addReadOnlyAttr(cl, "__class__", cl_, CLASS)
                cls.addReadOnlyAttr(cl, "im_self", cl_, ATTRIBUTE)
                cls.addReadOnlyAttr(cl, "__self__", cl_, ATTRIBUTE)

    @classmethod
    def addReadOnlyAttr(cls, cl, name, type_, kind):
        from pysonarsq.java.Builtins import Builtins

        b = Binding(name, Builtins.newDataModelUrl("the-standard-type-hierarchy"), type_, kind)
        cl.getTable().update(name, b)
        b.markSynthetic()
        b.markStatic()
        b.markReadOnly()

    @classmethod
    def missingReturn(cls, toType):
        from pysonarsq.java.Analyzer import Analyzer

        hasNone = False
        hasOther = False
        if toType.isUnionType():
            for t in toType.asUnionType().getTypes():
                if t == Analyzer.self.builtins.None_ or t == Analyzer.self.builtins.Cont:
                    hasNone = True
                else:
                    hasOther = True
        return hasNone and hasOther

    def __str__(self):
        """ generated source for method toString """
        return "<Call:" + str(self.func) + ":" + str(self.args) + ":" + str(self.start) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.func, v)
            self.visitNodeList(self.args, v)
            self.visitNodeList(self.keywords, v)
            self.visitNode(self.kwargs, v)
            self.visitNode(self.starargs, v)

