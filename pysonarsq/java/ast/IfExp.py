#!/usr/bin/env python
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type
from pysonarsq.java.types.UnionType import UnionType

from Node import Node

class IfExp(Node):

    def __init__(self, test, body, orelse, start, end):
        super(IfExp, self).__init__(start, end)
        self.test = test
        self.body = body
        self.orelse = orelse
        self.addChildren(test, body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        type1 = None
        type2 = None
        self.resolveExpr(self.test, s)
        if self.body is not None:
            type1 = self.resolveExpr(self.body, s)
        else:
            type1 = Analyzer.self.builtins.Cont
        if self.orelse is not None:
            type2 = self.resolveExpr(self.orelse, s)
        else:
            type2 = Analyzer.self.builtins.Cont
        return UnionType.union(type1, type2)

    def __str__(self):
        return "<IfExp:" + str(self.start) + ":" + str(self.test) + ":" + str(self.body) + ":" + str(self.orelse) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.test, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

