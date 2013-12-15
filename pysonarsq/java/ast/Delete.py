#!/usr/bin/env python
""" generated source for module Delete """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.ast.Name import Name

from java.util import List

from Node import Node

class Delete(Node):
    """ generated source for class Delete """

    def __init__(self, elts, start, end):
        super(Delete, self).__init__(start, end)
        self.targets = elts
        self.addChildren(elts)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        for n in self.targets:
            self.resolveExpr(n, s)
            if isinstance(n, (Name, )):
                s.remove(n.asName().id)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Delete:" + str(self.targets) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.targets, v)

