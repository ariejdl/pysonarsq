#!/usr/bin/env python
""" generated source for module BinOp """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from Node import Node

class BinOp(Node):


    def __init__(self, left, right, op, start, end):
        """ generated source for method __init__ """
        super(BinOp, self).__init__(start, end)
        self.left = left
        self.right = right
        self.op = op
        self.addChildren(left, right)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        ltype = None
        rtype = None
        if self.left is not None:
            ltype = self.resolveExpr(self.left, s)
        if self.right is not None:
            rtype = self.resolveExpr(self.right, s)
        #  If either non-null operand is a string, assume the result is a string.
        if ltype == Analyzer.self.builtins.BaseStr or rtype == Analyzer.self.builtins.BaseStr:
            return Analyzer.self.builtins.BaseStr
        #  If either non-null operand is a number, assume the result is a number.
        if ltype == Analyzer.self.builtins.BaseNum or rtype == Analyzer.self.builtins.BaseNum:
            return Analyzer.self.builtins.BaseNum
        if ltype is None:
            return (Analyzer.self.builtins.unknown if rtype is None else rtype)
        if rtype is None:
            return (Analyzer.self.builtins.unknown if ltype is None else ltype)
        return UnionType.union(ltype, rtype)

    def __str__(self):
        return "<BinOp:" + str(self.left) + " " + str(self.op) + " " + str(self.right) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.left, v)
            self.visitNode(self.right, v)

