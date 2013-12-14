#!/usr/bin/env python
""" generated source for module Index """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Index(Node):
    """ generated source for class Index """

    def __init__(self, n, start, end):
        """ generated source for method __init__ """
        super(Index, self).__init__(start, end)
        self.value = n
        self.addChildren(n)

    def resolve(self, s):
        """ generated source for method resolve """
        return self.resolveExpr(self.value, s)

    def __str__(self):
        """ generated source for method toString """
        return "<Index:" + str(self.value) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.value, v)

