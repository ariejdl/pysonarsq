#!/usr/bin/env python
""" generated source for module Expr """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node
# 
#  * Expression statement.
#  
class Expr(Node):
    """ generated source for class Expr """

    def __init__(self, n, start, end):
        """ generated source for method __init__ """
        super(Expr, self).__init__(start, end)
        self.value = n
        self.addChildren(n)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        if self.value is not None:
            self.resolveExpr(self.value, s)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        """ generated source for method toString """
        return "<Expr:" + str(self.value) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.value, v)

