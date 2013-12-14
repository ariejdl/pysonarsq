#!/usr/bin/env python
""" generated source for module AugAssign """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node
from Name import Name

class AugAssign(Node):

    def __init__(self, target, value, op, start, end):
        super(AugAssign, self).__init__(start, end)
        self.target = target
        self.value = value
        self.op = op
        self.addChildren(target, value)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        self.resolveExpr(self.target, s)
        self.resolveExpr(self.value, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<AugAssign:" + str(self.target) + " " + str(self.op) + "= " + str(self.value) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.target, v)
            self.visitNode(self.value, v)

