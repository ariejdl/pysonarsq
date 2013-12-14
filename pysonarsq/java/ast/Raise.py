#!/usr/bin/env python
""" generated source for module Raise """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Raise(Node):
    """ generated source for class Raise """

    def __init__(self, exceptionType, inst, traceback_, start, end):
        super(Raise, self).__init__(start, end)
        self.exceptionType = exceptionType
        self.inst = inst
        self.traceback_ = traceback_
        self.addChildren(exceptionType, inst, traceback_)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        if self.exceptionType is not None:
            self.resolveExpr(self.exceptionType, s)
        if self.inst is not None:
            self.resolveExpr(self.inst, s)
        if self.traceback_ is not None:
            self.resolveExpr(self.traceback_, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Raise:" + str(self.traceback_) + ":" + str(self.exceptionType) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.exceptionType, v)
            self.visitNode(self.inst, v)
            self.visitNode(self.traceback_, v)

