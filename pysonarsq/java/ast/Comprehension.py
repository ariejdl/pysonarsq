#!/usr/bin/env python
""" generated source for module Comprehension """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Binder import Binder

from pysonarsq.java.Binding import Binding

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Comprehension(Node):

    def __init__(self, target, _iter, ifs, start, end):
        super(Comprehension, self).__init__(start, end)
        self.target = target
        self.iter = _iter
        self.ifs = ifs
        self.addChildren(target, _iter)
        self.addChildren(ifs)

    def bindsName(self):
        return True

    def resolve(self, s):
        Binder.bindIter(s, self.target, self.iter, Binding.Kind.SCOPE)
        self.resolveList(self.ifs, s)
        return self.resolveExpr(self.target, s)

    def __str__(self):
        return "<Comprehension:" + str(self.start) + ":" + str(self.target) + ":" + str(self.iter) + ":" + str(self.ifs) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.target, v)
            self.visitNode(self.iter, v)
            self.visitNodeList(self.ifs, v)

