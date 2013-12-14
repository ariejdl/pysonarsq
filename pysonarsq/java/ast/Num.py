#!/usr/bin/env python
""" generated source for module Num """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Num(Node):
    """ generated source for class Num """

    def __init__(self, n, start, end):
        """ generated source for method __init__ """
        super(Num, self).__init__(start, end)
        self.n = n

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.BaseNum

    def __str__(self):
        """ generated source for method toString """
        return "<Num:" + str(self.n) + ">"

    def visit(self, v):
        """ generated source for method visit """
        v.visit(self)

