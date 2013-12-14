#!/usr/bin/env python
""" generated source for module Assert """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Assert(Node):

    def __init__(self, test, msg, start, end):
        super(Assert, self).__init__(start, end)
        self.test = test
        self.msg = msg
        self.addChildren(test, msg)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        if self.test is not None:
            self.resolveExpr(self.test, s)
        if self.msg is not None:
            self.resolveExpr(self.msg, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        """ generated source for method toString """
        return "<Assert:" + self.test + ":" + self.msg + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.test, v)
            self.visitNode(self.msg, v)

