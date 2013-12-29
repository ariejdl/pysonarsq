#!/usr/bin/env python
""" generated source for module Name """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

#from pysonarsq.java.Analyzer import Analyzer

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Name(Node):

    #@__init__.register(object, str, int, int)
    def __init__(self, id=None, start=None, end=None):
        super(Name, self).__init__()        

        self.id = id        
        self.start = start
        self.end = end 


    # 
    #      * Returns {@code true} if this name is structurally in a call position.
    #      * We don't always have enough information at this point to know
    #      * if it's a constructor call or a regular function/method call,
    #      * so we just determine if it looks like a call or not, and the
    #      * analyzer will convert constructor-calls to NEW in a later pass.
    #      
    def isCall(self):
        from Call import Call
    
        #  foo(...)
        if self.parent is not None and self.parent.isCall() and self == (self.parent).func:
            return True
        #  <expr>.foo(...)
        from Attribute import Attribute
        if isinstance(self.parent, (Attribute, )):
            gramps = self.parent.parent
            return self == (self.parent).attr and \
                isinstance(gramps, (Call, )) and \
                self.parent == (gramps).func
        return False

    def resolve(self, s):
        from pysonarsq.java.Scope import Scope        
        from pysonarsq.java.Analyzer import Analyzer

        b = s.lookup(self.id)
        if b is not None:
            Analyzer.self.putRef(self, b)
            Analyzer.self.stats.inc("resolved")
            return Scope.makeUnion(b)
        elif self.id == "True" or self.id == "False":
            return Analyzer.self.builtins.BaseBool
        else:
            Analyzer.self.putProblem(self, "unbound variable " + self.id)
            Analyzer.self.stats.inc("unresolved")
            t = Analyzer.self.builtins.unknown;
            t.getTable().setPath(s.extendPath(self.id))
            return t

    # 
    #      * Returns {@code true} if this name node is the {@code attr} child
    #      * (i.e. the attribute being accessed) of an {@link Attribute} node.
    #      
    def isAttribute(self):
        return isinstance(parent, (Attribute, )) and (parent).getAttr() == self

    def __str__(self):
        return "<Name:" + str(self.start) + ":" + str(self.end) + ":" + str(self.id) + ">"

    def toDisplay(self):
        return self.id

    def visit(self, v):
        v.visit(self)

