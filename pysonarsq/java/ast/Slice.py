#!/usr/bin/env python
""" generated source for module Slice """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from Node import Node

class Slice(Node):
    def __init__(self, lower, step, upper, start, end):
        super(Slice, self).__init__(start, end)
        self.lower = lower
        self.step = step
        self.upper = upper
        self.addChildren(lower, step, upper)

    def resolve(self, s):
        if self.lower is not None:
            self.resolveExpr(self.lower, s)
        if self.step is not None:
            self.resolveExpr(self.step, s)
        if self.upper is not None:
            self.resolveExpr(self.upper, s)
        return ListType()

    def __str__(self):
        return "<Slice:" + str(self.lower) + ":" + str(self.step) + ":" + str(self.upper) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.lower, v)
            self.visitNode(self.step, v)
            self.visitNode(self.upper, v)

