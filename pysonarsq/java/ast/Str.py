#!/usr/bin/env python
""" generated source for module Str """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.types.Type import Type

from Node import Node

class Str(Node):

    def __init__(self, value, start, end):
        super(Str, self).__init__(start, end)
        #self.value = str(value)
        self.value = value.encode('utf-8')

    def getStr(self):
        return self.value

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        return Analyzer.self.builtins.BaseStr

    def __str__(self):
        return "<Str>"

    def visit(self, v):
        v.visit(self)

