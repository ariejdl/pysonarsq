#!/usr/bin/env python
""" generated source for module YieldFrom """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from Node import Node

class YieldFrom(Node):
    """ generated source for class YieldFrom """
    def __init__(self, n, start, end):
        """ generated source for method __init__ """
        super(YieldFrom, self).__init__(start, end)
        self.value = n
        self.addChildren(n)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        if self.value is not None:
            return ListType(resolveExpr(self.value, s))
        else:
            return Analyzer.self.builtins.None_

    def __str__(self):
        """ generated source for method toString """
        return "<YieldFrom:" + start + ":" + self.value + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.value, v)

