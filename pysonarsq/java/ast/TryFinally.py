#!/usr/bin/env python
""" generated source for module TryFinally """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node
from Block import Block

class TryFinally(Node):
    """ generated source for class TryFinally """

    def __init__(self, body, orelse, start, end):
        """ generated source for method __init__ """
        super(TryFinally, self).__init__(start, end)
        self.body = body
        self.finalbody = orelse
        self.addChildren(body, orelse)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        tFinal = Analyzer.self.builtins.unknown
        if self.body is not None:
            self.resolveExpr(self.body, s)
        if self.finalbody is not None:
            tFinal = resolveExpr(self.finalbody, s)
        return tFinal

    def __str__(self):
        """ generated source for method toString """
        return "<TryFinally:" + self.body + ":" + self.finalbody + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.body, v)
            self.visitNode(self.finalbody, v)

