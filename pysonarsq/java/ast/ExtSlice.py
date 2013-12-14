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
    """ generated source for class ExtSlice """

    def __init__(self, dims, start, end):
        """ generated source for method __init__ """
        super(ExtSlice, self).__init__(start, end)
        self.dims = dims
        self.addChildren(dims)

    def resolve(self, s):
        """ generated source for method resolve """
        for d in dims:
            d.resolve(s)
        return ListType()

    def __str__(self):
        """ generated source for method toString """
        return "<ExtSlice:" + self.dims + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            for d in dims:
                self.visitNode(d, v)

