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
    """ generated source for class SetComp """


    def __init__(self, elt, generators, start, end):
        """ generated source for method __init__ """
        super(SetComp, self).__init__(start, end)
        self.elt = elt
        self.generators = generators
        self.addChildren(elt)
        self.addChildren(generators)

    def resolve(self, s):
        """ generated source for method resolve """
        resolveList(self.generators, s)
        return ListType(resolveExpr(self.elt, s))

    def __str__(self):
        """ generated source for method toString """
        return "<NSetComp:" + start + ":" + self.elt + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.elt, v)
            self.visitNodeList(self.generators, v)

