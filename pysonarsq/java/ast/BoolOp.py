#!/usr/bin/env python
""" generated source for module BoolOp """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node
from Name import Name

class BoolOp(Node):

    def __init__(self, op, values, start, end):
        super(BoolOp, self).__init__(start, end)
        self.op = op
        self.values = values
        self.addChildren(values)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        if self.op.id == "and":
            for e in values:
                last = resolveExpr(e, s)
            return (Analyzer.self.builtins.unknown if last is None else last)
        #  OR
        return resolveListAsUnion(self.values, s)

    def __str__(self):
        return "<BoolOp:" + str(self.op) + ":" + str(self.values) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.values, v)

