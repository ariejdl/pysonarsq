#!/usr/bin/env python
""" generated source for module Return """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Return(Node):
    def __init__(self, n, start, end):
        super(Return, self).__init__(start, end)
        self.value = n
        self.addChildren(n)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        if self.value is None:
            return Analyzer.self.builtins.None_
        else:
            return self.resolveExpr(self.value, s)

    def __str__(self):
        return "<Return:" + str(self.value) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.value, v)

