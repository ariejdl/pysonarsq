#!/usr/bin/env python
""" generated source for module InstanceType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope


from java.util import List

from Type import Type


class InstanceType(Type):

    #@__init__.register(object, Type, Call, List)
    def __init__(self, c, call=None, args=None):
        super(InstanceType, self).__init__()
        
        self.getTable().setScopeType(Scope.ScopeType.INSTANCE)
        self.getTable().addSuper(c.getTable())
        self.getTable().setPath(c.getTable().getPath())
        
        self.classType = c   

        from pysonarsq.java.ast.Call import Call     
        
        if args is not None:
            initFunc = self.getTable().lookupAttrType("__init__")
            if initFunc is not None and initFunc.isFuncType() and initFunc.asFuncType().getFunc() is not None:
                initFunc.asFuncType().setSelfType(self)
                Call.apply(initFunc.asFuncType(), args, None, None, None, call)
                initFunc.asFuncType().setSelfType(None)

    def getClassType(self):
        return self.classType

    def __eq__(self, other):
        if isinstance(other, (InstanceType, )):
            iother = other # there is a cast!
            if self.classType == iother.classType and self.getTable().keySet() == iother.getTable().keySet():
                return True
        return False

    def hashCode(self):
        return hash(self.classType)

    def printType(self, ctr):
        #return self.getClassType().asClassType().__name__
        return self.getClassType().name

