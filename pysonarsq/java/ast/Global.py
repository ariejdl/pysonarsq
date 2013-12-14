#!/usr/bin/env python
""" generated source for module Global """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


#from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Global(Node):

    def __init__(self, names, start, end):
        super(Global, self).__init__(start, end)
        self.names = names
        self.addChildren(names)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        #  Do nothing here because global names are processed by NBlock
        return Analyzer.self.builtins.Cont

    def getNames(self):
        return self.names

    def __str__(self):
        return "<Global:" + str(self.names) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.names, v)

