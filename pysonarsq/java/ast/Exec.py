#!/usr/bin/env python
""" generated source for module Exec """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Exec(Node):
    """ generated source for class Exec """

    def __init__(self, body, globals, locals, start, end):
        """ generated source for method __init__ """
        super(Exec, self).__init__(start, end)
        self.body = body
        self.globals = globals
        self.locals = locals
        self.addChildren(body, globals, locals)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        if self.body is not None:
            self.resolveExpr(self.body, s)
        if self.globals is not None:
            self.resolveExpr(self.globals, s)
        if self.locals is not None:
            self.resolveExpr(self.locals, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        """ generated source for method toString """
        return "<Exec:" + start + ":" + end + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.body, v)
            self.visitNode(self.globals, v)
            self.visitNode(self.locals, v)

