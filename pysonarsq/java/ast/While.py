#!/usr/bin/env python
""" generated source for module While """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from Node import Node
from Block import Block

class While(Node):
    """ generated source for class While """

    def __init__(self, test, body, orelse, start, end):
        """ generated source for method __init__ """
        super(While, self).__init__(start, end)
        self.test = test
        self.body = body
        self.orelse = orelse
        self.addChildren(test, body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        self.resolveExpr(self.test, s)
        t = Analyzer.self.builtins.unknown
        if self.body is not None:
            t = resolveExpr(self.body, s)
        if self.orelse is not None:
            t = UnionType.union(t, resolveExpr(self.orelse, s))
        return t

    def __str__(self):
        """ generated source for method toString """
        return "<While:" + self.test + ":" + self.body + ":" + self.orelse + ":" + start + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.test, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

