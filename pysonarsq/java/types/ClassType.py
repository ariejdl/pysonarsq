#!/usr/bin/env python
""" generated source for module ClassType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from Type import Type

class ClassType(Type):
    """ generated source for class ClassType """
    name = str()
    canon = None


    #@overloaded
    def __init__(self, name, parent, superClass=None):
        from pysonarsq.java.Scope import Scope
        self.superclass = None

        super(ClassType, self).__init__()
        self.name = name
        self.setTable(Scope(parent, Scope.ScopeType.CLASS))
        self.getTable().setType(self)
        if parent is not None:
            self.getTable().setPath(parent.extendPath(name))
        else:
            self.getTable().setPath(name)
            
        if superClass is not None:
            self.addSuper(superClass)            

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addSuper(self, superclass):
        self.superclass = superclass
        self.getTable().addSuper(superclass.getTable())

    def getCanon(self):
        from InstanceType import InstanceType

        if self.canon is None:
            self.canon = InstanceType(self, None, None)
        return self.canon

    def __eq__(self, other):
        return self is other # java's equals seems to do this
        
    def hashCode(self):
        return hash("ClassType")        

    def printType(self, ctr):
        sb = []
        sb.append("<")
        sb.append(self.getName())
        sb.append(">")
        return ''.join(sb)

