#!/usr/bin/env python
""" generated source for module TryExcept """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from java.util import List

from Node import Node
from Block import Block

class TryExcept(Node):

    def __init__(self, handlers, body, orelse, start, end):
        super(TryExcept, self).__init__(start, end)
        self.handlers = handlers
        self.body = body
        self.orelse = orelse
        self.addChildren(handlers)
        self.addChildren(body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        tp1 = Analyzer.self.builtins.unknown
        tp2 = Analyzer.self.builtins.unknown
        tph = Analyzer.self.builtins.unknown
        for h in self.handlers:
            tph = UnionType.union(tph, self.resolveExpr(h, s))
        if self.body is not None:
            tp1 = self.resolveExpr(self.body, s)
        if self.orelse is not None:
            tp2 = self.resolveExpr(self.orelse, s)
        return UnionType.union(tp1, UnionType.union(tp2, tph))

    def __str__(self):
        return "<TryExcept:" + str(self.handlers) + ":" + str(self.body) + ":" + str(self.orelse) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.handlers, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

