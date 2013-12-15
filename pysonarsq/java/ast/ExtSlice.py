#!/usr/bin/env python
""" generated source for module ExtSlice """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class ExtSlice(Node):

    def __init__(self, dims, start, end):
        super(ExtSlice, self).__init__(start, end)
        self.dims = dims
        self.addChildren(dims)

    def resolve(self, s):
        for d in self.dims:
            d.resolve(s)
        return ListType()

    def __str__(self):
        return "<ExtSlice:" + str(self.dims) + ">"

    def visit(self, v):
        if v.visit(self):
            for d in self.dims:
                self.visitNode(d, v)

