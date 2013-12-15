#!/usr/bin/env python
""" generated source for module Keyword """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type


from Node import Node
# 
#  * Represents a keyword argument (name=value) in a function call.
#  
class Keyword(Node):

    def __init__(self, arg, value, start, end):

        super(Keyword, self).__init__(start, end)
        self.arg = arg
        self.value = value
        self.addChildren(value)

    def resolve(self, s):
        return self.resolveExpr(self.value, s)

    def getArg(self):
        return self.arg

    def getValue(self):
        return self.value

    def __str__(self):
        return "<Keyword:" + str(self.arg) + ":" + str(self.value) + ">"

    def toDisplay(self):
        return self.arg

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.value, v)

