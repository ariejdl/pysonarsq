#!/usr/bin/env python:

""" generated source for module Assign """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Binder import Binder

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Assign(Node):

    def __init__(self, targets, rvalue, start, end):
        super(Assign, self).__init__(start, end)
        self.targets = targets
        self.rvalue = rvalue
        self.addChildren(targets)
        self.addChildren(rvalue)

    def bindsName(self):
        return True

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        if self.rvalue is None:
            Analyzer.self.putProblem(self, "missing RHS of assignment")
        else:
            valueType = self.resolveExpr(self.rvalue, s);
            for t in self.targets:
                Binder.bind(s, t, valueType)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Assign:" + str(self.targets) + "=" + str(self.rvalue) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.targets, v)
            self.visitNode(self.rvalue, v)

