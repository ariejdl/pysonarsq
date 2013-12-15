#!/usr/bin/env python
""" generated source for module SetComp """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class SetComp(Node):

    def __init__(self, elt, generators, start, end):
        super(SetComp, self).__init__(start, end)
        self.elt = elt
        self.generators = generators
        self.addChildren(elt)
        self.addChildren(generators)

    def resolve(self, s):
        self.resolveList(self.generators, s)
        return ListType(self.resolveExpr(self.elt, s))

    def __str__(self):
        return "<NSetComp:" + str(self.start) + ":" + str(self.elt) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.elt, v)
            self.visitNodeList(self.generators, v)

