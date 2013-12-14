#!/usr/bin/env python
""" generated source for module For """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Binder import Binder

from pysonarsq.java.Binding import Binding

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type
from pysonarsq.java.types.UnionType import UnionType

from Node import Node
from Block import Block

class For(Node):

    def __init__(self, target, iter, body, orelse, start, end):
        super(For, self).__init__(start, end)
        self.target = target
        self.iter = iter
        self.body = body
        self.orelse = orelse
        self.addChildren(target, iter, body, orelse)

    def bindsName(self):
        return True

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        Binder.bindIter(s, self.target, self.iter, Binding.Kind.SCOPE)
        ret = None
        if self.body is None:
            ret = Analyzer.self.builtins.unknown
        else:
            ret = self.resolveExpr(self.body, s)
        if self.orelse is not None:
            ret = UnionType.union(ret, self.resolveExpr(self.orelse, s))
        return ret

    def __str__(self):
        return "<For:" + str(self.target) + ":" + str(self.iter) + ":" + str(self.body) + ":" + str(self.orelse) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.target, v)
            self.visitNode(self.iter, v)
            self.visitNode(self.body, v)
            self.visitNode(self.orelse, v)

