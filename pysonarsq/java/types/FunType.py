#!/usr/bin/env python
""" generated source for module FunType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.Scope import Scope

from pysonarsq.java.TypeStack import TypeStack

from pysonarsq.java.ast import *
from pysonarsq.java.ast.FunctionDef import FunctionDef

from java.util import HashMap
from java.util import List

from pysonarsq.java._ import _
from TupleType import TupleType

from Type import Type

class FunType(Type):
    """ generated source for class FunType """


    #@__init__.register(object, FunctionDef, Scope)
    def __init__(self, func=None, env=None):
        self.arrows = HashMap()
        self.cls = None
        self.defaultTypes = List()        
        
        self.selfType = None
        self.func = None
        from pysonarsq.java.Analyzer import Analyzer
        
        super(FunType, self).__init__()   
        self.env = None     
        if isinstance(func, FunctionDef):
            self.func = func
            self.env = env
        elif isinstance(func, Type):
            from_, to = func, env
            self.addMapping(from_, to)
            self.getTable().addSuper(Analyzer.self.builtins.BaseFunction.getTable())
            self.getTable().setPath(Analyzer.self.builtins.BaseFunction.getTable().getPath())            

    def addMapping(self, from_, to):
        if len(self.arrows) < 5:
            self.arrows[from_] = to
            oldArrows = self.arrows;
            self.arrows = self.compressArrows(self.arrows)
            if len(str(self)) > 900:
                self.arrows = oldArrows

    def getMapping(self, from_):
        return self.arrows.get(from_)

    def getReturnType(self):
        from pysonarsq.java.Analyzer import Analyzer
        
        if not _.isEmpty(self.arrows):
            #return self.arrows.values().iterator().next()
            return self.arrows.values()[0]
        else:
            return Analyzer.self.builtins.unknown

    def getFunc(self):
        return self.func

    def getEnv(self):
        return self.env

    def getCls(self):
        return self.cls

    def setCls(self, cls):
        self.cls = cls

    def getSelfType(self):
        return self.selfType

    def setSelfType(self, selfType):
        self.selfType = selfType

    def clearSelfType(self):
        self.selfType = None

    def getDefaultTypes(self):
        return self.defaultTypes

    def setDefaultTypes(self, defaultTypes):
        self.defaultTypes = defaultTypes

    def __eq__(self, other):
        if isinstance(other, (FunType, )):
            fo = other # cast in java code, should have been picked up by java2python
            return fo.getTable().getPath() == self.getTable().getPath() or self is other
        else:
            return False

    @classmethod
    def removeNoneReturn(cls, toType):
        from pysonarsq.java.Analyzer import Analyzer
        
        """ generated source for method removeNoneReturn """
        if toType.isUnionType():
            types.remove(Analyzer.self.builtins.Cont)
            return UnionType.newUnion(types)
        else:
            return toType

    def hashCode(self):
        return hash("FunType")

    def subsumed(self, type1, type2):
        return self.subsumedInner(type1, type2, TypeStack())

    def subsumedInner(self, type1, type2, typeStack):
        from pysonarsq.java.Analyzer import Analyzer
        
        if typeStack.contains(type1, type2):
            return True
        if type1.isUnknownType() or type1 == Analyzer.self.builtins.None_ or type1 == type2:
            return True
        if isinstance(type1, (TupleType, )) and isinstance(type2, (TupleType, )):
            elems1 = type1.getElementTypes();
            elems2 = type2.getElementTypes();            
            
            if len(elems1) == len(elems2):
                typeStack.push(type1, type2)
                for i in range(len(elems1)):
                    if not self.subsumedInner(elems1[i], elems2[i], self.typeStack):
                        self.typeStack.pop(type1, type2)
                        return False
            return True
        return False

    def compressArrows(self, arrows):
        ret = HashMap()
        for e1 in arrows.items():
            subsumed = False
            
            for e2 in arrows.items():
                if e1 != e2 and self.subsumed(e1[0], e2[0]):
                    subsumed = True
                    break
            if not subsumed:
                ret[e1[0]] = e1[1]
        return ret

    def printType(self, ctr):
        from pysonarsq.java.Analyzer import Analyzer
        
        if _.isEmpty(self.arrows):
            return "? -> ?"
            
        sb = []
        num = ctr.visit(self)
        if num is not None:
            sb.append("#")
            sb.append(num)
        else:
            newNum = ctr.push(self);
            
            i = 0;
            seen = set()
            for e in self.arrows.items():
                as_ = e[0].printType(ctr) + " -> " + e[1].printType(ctr);
                if not as_ in seen:
                    if i != 0:
                        if Analyzer.self.multilineFunType:
                            sb.append("\n| ")
                        else:
                            sb.append(" | ")
                    sb.append(as_)
                    seen.add(as_)
                i += 1
            if ctr.isUsed(self):
                sb.append("=#")
                sb.append(newNum)
                sb.append(": ")
            ctr.pop(self)
            
        return ''.join(map(str,sb))

