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
    """ generated source for class Keyword """

    def __init__(self, arg, value, start, end):
        """ generated source for method __init__ """
        super(Keyword, self).__init__(start, end)
        self.arg = arg
        self.value = value
        self.addChildren(value)

    def resolve(self, s):
        """ generated source for method resolve """
        return resolveExpr(self.value, s)

    def getArg(self):
        """ generated source for method getArg """
        return self.arg

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def __str__(self):
        """ generated source for method toString """
        return "<Keyword:" + self.arg + ":" + self.value + ">"

    def toDisplay(self):
        """ generated source for method toDisplay """
        return self.arg

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.value, v)

