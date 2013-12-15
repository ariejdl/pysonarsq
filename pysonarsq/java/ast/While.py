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

    def __init__(self, test, body, orelse, start, end):
        super(While, self).__init__(start, end)
        self.test = test
        self.body = body
        self.orelse = orelse
        self.addChildren(test, body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        self.resolveExpr(self.test, s)
        t = Analyzer.self.builtins.unknown
        if self.body is not None:
            t = self.resolveExpr(self.body, s)
        if self.orelse is not None:
            t = UnionType.union(t, self.resolveExpr(self.orelse, s))
        return t

    def __str__(self):
        return "<While:" + str(self.test) + ":" + str(self.body) + ":" + str(self.orelse) + ":" + str(self.start) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.test, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

