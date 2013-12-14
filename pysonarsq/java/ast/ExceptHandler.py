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
    """ generated source for class ExceptHandler """

    def __init__(self, name, exceptionType, body, start, end):
        """ generated source for method __init__ """
        super(ExceptHandler, self).__init__(start, end)
        self.name = name
        self.exceptionType = exceptionType
        self.body = body
        self.addChildren(name, exceptionType, body)

    def bindsName(self):
        """ generated source for method bindsName """
        return True

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        typeval = Analyzer.self.builtins.unknown
        if self.exceptionType is not None:
            typeval = resolveExpr(self.exceptionType, s)
        if self.name is not None:
            Binder.bind(s, self.name, typeval)
        if self.body is not None:
            return resolveExpr(self.body, s)
        else:
            return Analyzer.self.builtins.unknown

    def __str__(self):
        """ generated source for method toString """
        return "<ExceptHandler:" + start + ":" + self.name + ":" + self.exceptionType + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.name, v)
            self.visitNode(self.exceptionType, v)
            self.visitNode(self.body, v)

