#!/usr/bin/env python
""" generated source for module FunctionDef """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.Binder import Binder

from pysonarsq.java.types.Type import Type

from java.util import ArrayList

from java.util import List

from Node import Node
from Name import Name

class FunctionDef(Node):
    """
    name = Name()
    args = List()
    defaults = List()
    defaultTypes = List()
    vararg = Name()

    #  *args
    kwarg = Name()

    #  **kwarg
    body = Node()
    decoratorList = List()
    called = False
     """    

    def __init__(self, name=None, args=[], body=None, defaults=None, vararg=None, kwarg=None, start=None, end=None):
        super(FunctionDef, self).__init__(start, end)
        
        self.name = None
        if name is not None:
            self.name = name
            
        self.called = False
        self.decoratorList = List()
        
        self.body = body
        self.args = args
        self.defaults = defaults
        self.vararg = vararg
        self.kwarg = kwarg
        
        self.addChildren(name)
        self.addChildren(args)
        self.addChildren(defaults)
        self.addChildren(vararg, kwarg, self.body)
        
    def setDecoratorList(self, decoratorList):
        self.decoratorList = decoratorList
        self.addChildren(decoratorList)

    def getDecoratorList(self):
        if self.decoratorList is None:
            self.decoratorList = ArrayList()
        return self.decoratorList

    def isFunctionDef(self):
        return True

    def bindsName(self):
        return True

    # 
    #      * Returns the name of the function for indexing/qname purposes.
    #      * Lambdas will return a generated name.
    #      
    def getBindingName(self, s):
        return self.name.id

    def getArgs(self):
        return self.args

    def getDefaults(self):
        return self.defaults

    def getDefaultTypes(self):
        return self.defaultTypes

    def getBody(self):
        return self.body

    def getName(self):
        return self.name

    # 
    #      * @return the vararg
    #      
    def getVararg(self):
        return self.vararg

    # 
    #      * @param vararg the vararg to set
    #      
    def setVararg(self, vararg):
        self.vararg = vararg

    # 
    #      * @return the kwarg
    #      
    def getKwarg(self):
        return self.kwarg

    # 
    #      * @param kwarg the kwarg to set
    #      
    def setKwarg(self, kwarg):
        self.kwarg = kwarg

    # 
    #      * A function's environment is not necessarily the enclosing scope. A
    #      * method's environment is the scope of the most recent scope that is not a
    #      * class.
    #      * <p/>
    #      * Be sure to distinguish the environment and the symbol table. The
    #      * function's table is only used for the function's attributes like
    #      * "im_class". Its parent should be the table of the enclosing scope, and
    #      * its path should be derived from that scope too for locating the names
    #      * "lexically".
    #      
    def resolve(self, outer):
        from pysonarsq.java.Binding import Binding
        from pysonarsq.java.types.FunType import FunType
        from pysonarsq.java.Analyzer import Analyzer
        from pysonarsq.java.Scope import Scope
        
        self.resolveList(self.decoratorList, outer)
        # XXX: not handling functional transformations yet
        fun = FunType(self, outer.getForwarding())
        fun.getTable().setParent(outer)
        fun.getTable().setPath(outer.extendPath(self.name.id))
        fun.setDefaultTypes(self.resolveAndConstructList(self.defaults, outer))
        Analyzer.self.addUncalled(fun)
        
        funkind = Binding.Kind()
        if outer.getScopeType() == Scope.ScopeType.CLASS:
            if "__init__" == self.name.id:
                funkind = Binding.Kind.CONSTRUCTOR
            else:
                funkind = Binding.Kind.METHOD
        else:
            funkind = Binding.Kind.FUNCTION
            
        outType = outer.getType()
        if outType is not None and outType.isClassType():
            fun.setCls(outType.asClassType())
            
        Binder.bind(outer, self.name, fun, funkind)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Function:" + str(self.start) + ":" + str(self.name) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.name, v)
            self.visitNodeList(self.args, v)
            self.visitNodeList(self.defaults, v)
            self.visitNode(self.kwarg, v)
            self.visitNode(self.vararg, v)
            self.visitNode(self.body, v)

    def __eq__(self, obj):
        if isinstance(obj, (FunctionDef, )):
            return (fo.getFile() == getFile() and fo.start == start)
        else:
            return False

