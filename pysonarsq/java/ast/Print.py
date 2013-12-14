#!/usr/bin/env python
""" generated source for module Print """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Print(Node):
    """ generated source for class Print """

    def __init__(self, dest, elts, start, end):
        super(Print, self).__init__(start, end)
        self.dest = dest
        self.values = elts
        self.addChildren(dest)
        self.addChildren(elts)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        if self.dest is not None:
            self.resolveExpr(self.dest, s)
        if self.values is not None:
            self.resolveList(self.values, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Print:" + str(self.values) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.dest, v)
            self.visitNodeList(self.values, v)

