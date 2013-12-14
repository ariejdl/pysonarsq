#!/usr/bin/env python
""" generated source for module Str """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.types.Type import Type

from Node import Node

class Str(Node):
    """ generated source for class Str """

    def __init__(self, value, start, end):
        """ generated source for method __init__ """
        super(Str, self).__init__(start, end)
        self.value = str(value)

    def getStr(self):
        """ generated source for method getStr """
        return self.value

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.BaseStr

    def __str__(self):
        """ generated source for method toString """
        return "<Str>"

    def visit(self, v):
        """ generated source for method visit """
        v.visit(self)

