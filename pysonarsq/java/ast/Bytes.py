#!/usr/bin/env python
""" generated source for module Bytes """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Bytes(Node):
    """ generated source for class Bytes """

    def __init__(self, value, start, end):
        """ generated source for method __init__ """
        super(Bytes, self).__init__(start, end)
        self.value = value.__str__()

    def getStr(self):
        """ generated source for method getStr """
        return self.value

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.BaseStr

    def __str__(self):
        """ generated source for method toString """
        return "<Bytpes: " + self.value + ">"

    def visit(self, v):
        """ generated source for method visit """
        v.visit(self)

