#!/usr/bin/env python
""" generated source for module With """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Binder import Binder

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node
from Block import Block

class With(Node):
    """ generated source for class With """

    def __init__(self, items, body, start, end):
        """ generated source for method __init__ """
        super(With, self).__init__(start, end)
        self.items = items
        self.body = body
        self.addChildren(items)
        self.addChildren(body)

    def resolve(self, s):
        """ generated source for method resolve """
        for item in items:
            if item.optional_vars is not None:
                Binder.bind(s, item.optional_vars, val)
        return resolveExpr(self.body, s)

    def __str__(self):
        """ generated source for method toString """
        return "<With:" + self.items + ":" + self.body + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            for item in items:
                self.visitNode(item, v)
            self.visitNode(self.body, v)

