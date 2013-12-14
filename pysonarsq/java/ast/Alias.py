#!/usr/bin/env python
""" generated source for module Alias """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node
from Name import Name

class Alias(Node):

    def __init__(self, name, asname, start, end):
        super(Alias, self).__init__(start, end)
        self.name = name
        self.asname = asname
        self.addChildren(name)
        self.addChildren(asname)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.unknown

    def __str__(self):
        """ generated source for method toString """
        return "<Alias:" + self.name + " as " + self.asname + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            for n in self.name:
                self.visitNode(n, v)
            self.visitNode(self.asname, v)

