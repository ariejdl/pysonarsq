#!/usr/bin/env python
""" generated source for module ExceptHandler """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Binder import Binder

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node
from Block import Block

class ExceptHandler(Node):

    def __init__(self, name, exceptionType, body, start, end):
        super(ExceptHandler, self).__init__(start, end)
        self.name = name
        self.exceptionType = exceptionType
        self.body = body
        self.addChildren(name, exceptionType, body)

    def bindsName(self):
        return True

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        typeval = Analyzer.self.builtins.unknown
        if self.exceptionType is not None:
            typeval = self.resolveExpr(self.exceptionType, s)
        if self.name is not None:
            Binder.bind(s, self.name, typeval)
        if self.body is not None:
            return self.resolveExpr(self.body, s)
        else:
            return Analyzer.self.builtins.unknown

    def __str__(self):
        return "<ExceptHandler:" + str(self.start) + ":" + str(self.name) + ":" + str(self.exceptionType) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.name, v)
            self.visitNode(self.exceptionType, v)
            self.visitNode(self.body, v)

