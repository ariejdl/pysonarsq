#!/usr/bin/env python
""" generated source for module Compare """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Compare(Node):
     
    def __init__(self, left, ops, comparators, start, end):
        super(Compare, self).__init__(start, end)
        self.left = left
        self.ops = ops
        self.comparators = comparators
        self.addChildren(left)
        self.addChildren(ops)
        self.addChildren(comparators)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        self.resolveExpr(self.left, s)
        self.resolveList(self.comparators, s)
        return Analyzer.self.builtins.BaseNum

    def __str__(self):
        return "<Compare:" + str(self.left) + ":" + str(self.ops) + ":" + str(self.comparators) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.left, v)
            self.visitNodeList(self.ops, v)
            self.visitNodeList(self.comparators, v)

