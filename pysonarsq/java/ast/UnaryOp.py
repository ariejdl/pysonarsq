#!/usr/bin/env python
""" generated source for module UnaryOp """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class UnaryOp(Node):

    def __init__(self, op, n, start, end):
        super(UnaryOp, self).__init__(start, end)
        self.op = op
        self.operand = n
        self.addChildren(op, n)

    def resolve(self, s):
        return self.resolveExpr(self.operand, s)

    def __str__(self):
        return "<UOp:" + str(self.op) + ":" + str(self.operand) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.op, v)
            self.visitNode(self.operand, v)

