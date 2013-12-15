#!/usr/bin/env python
""" generated source for module Set """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from java.util import List


from Sequence import Sequence

class Set(Sequence):
    def __init__(self, elts, start, end):
        super(Set, self).__init__(elts, start, end)

    def resolve(self, s):
        if len(self.elts) == 0:
            return ListType()
        listType = None
        for elt in self.elts:
            if listType is None:
                listType = ListType(self.resolveExpr(elt, s))
            else:
                listType.add(self.resolveExpr(elt, s))
        return listType

    def __str__(self):
        return "<List:" + str(self.start) + ":" + str(self.elts) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.elts, v)

