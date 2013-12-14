#!/usr/bin/env python
""" generated source for module Delete """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Delete(Node):
    """ generated source for class Delete """

    def __init__(self, elts, start, end):
        """ generated source for method __init__ """
        super(Delete, self).__init__(start, end)
        self.targets = elts
        self.addChildren(elts)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        for n in targets:
            self.resolveExpr(n, s)
            if isinstance(n, (Name, )):
                s.remove(n.asName().id)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        """ generated source for method toString """
        return "<Delete:" + self.targets + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNodeList(self.targets, v)

