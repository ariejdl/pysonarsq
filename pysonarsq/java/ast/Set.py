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
    """ generated source for class Set """
    def __init__(self, elts, start, end):
        """ generated source for method __init__ """
        super(Set, self).__init__(start, end)

    def resolve(self, s):
        """ generated source for method resolve """
        if len(elts) == 0:
            return ListType()
        listType = None
        for elt in elts:
            if listType is None:
                listType = ListType(resolveExpr(elt, s))
            else:
                listType.add(resolveExpr(elt, s))
        return listType

    def __str__(self):
        """ generated source for method toString """
        return "<List:" + start + ":" + elts + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNodeList(elts, v)

