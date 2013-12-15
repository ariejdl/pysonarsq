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

    def __init__(self, items, body, start, end):
        super(With, self).__init__(start, end)
        self.items = items
        self.body = body
        self.addChildren(items)
        self.addChildren(body)

    def resolve(self, s):
        for item in self.items:
            if item.optional_vars is not None:
                val = self.resolveExpr(item.context_expr, s);
                Binder.bind(s, item.optional_vars, val)
        return self.resolveExpr(self.body, s)

    def __str__(self):
        return "<With:" + str(self.items) + ":" + str(self.body) + ">"

    def visit(self, v):
        if v.visit(self):
            for item in self.items:
                self.visitNode(item, v)
            self.visitNode(self.body, v)

