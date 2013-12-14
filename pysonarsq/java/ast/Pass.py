#!/usr/bin/env python
""" generated source for module Pass """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

class Pass(Node):
    """ generated source for class Pass """
    def __init__(self, start, end):
        """ generated source for method __init__ """
        super(Pass, self).__init__(start, end)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.Cont

    def __str__(self):
        """ generated source for method toString """
        return "<Pass>"

    def visit(self, v):
        """ generated source for method visit """
        v.visit(self)

