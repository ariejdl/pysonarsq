#!/usr/bin/env python
""" generated source for module If """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from Node import Node
from Block import Block

class If(Node):
    """ generated source for class If """

    def __init__(self, test, body, orelse, start, end):
        """ generated source for method __init__ """
        super(If, self).__init__(start, end)
        self.test = test
        self.body = body
        self.orelse = orelse
        self.addChildren(test, body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        type1 = None
        type2 = None
        self.resolveExpr(self.test, s)
        s1 = s.copy()
        s2 = s.copy()
        
        if self.body is not None and not self.body.isEmpty():
            type1 = self.resolveExpr(self.body, s1)
        else:
            type1 = Analyzer.self.builtins.Cont
            
        if self.orelse is not None and not self.orelse.isEmpty():
            type2 = self.resolveExpr(self.orelse, s2)
        else:
            type2 = Analyzer.self.builtins.Cont
            
        cont1 = UnionType.contains(type1, Analyzer.self.builtins.Cont)
        cont2 = UnionType.contains(type2, Analyzer.self.builtins.Cont)
        
        if cont1 and cont2:
            s.overwrite(Scope.merge(s1, s2))
        elif cont1:
            s.overwrite(s1)
        elif cont2:
            s.overwrite(s2)
            
        return UnionType.union(type1, type2)

    def __str__(self):
        return "<If:" + str(self.start) + ":" + str(self.test) + ":" + str(self.body) + ":" + str(self.orelse) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.test, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

