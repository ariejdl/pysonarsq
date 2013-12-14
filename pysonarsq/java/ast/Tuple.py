#!/usr/bin/env python
""" generated source for module Tuple """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

#from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.TupleType import TupleType

from pysonarsq.java.types.Type import Type

from java.util import List


from Sequence import Sequence

class Tuple(Sequence):
    """ generated source for class Tuple """
    def __init__(self, elts, start, end):
        super(Tuple, self).__init__(elts, start, end)

    def resolve(self, s):
        t = TupleType()
        for e in self.elts:
            t.add(self.resolveExpr(e, s))
        return t

    def __str__(self):
        return "<Tuple:" + str(self.start) + ":" + str(self.elts) + ">"

    def toDisplay(self):
        """ generated source for method toDisplay """
        sb = []
        sb.append("(")
        idx = 0
        for n in elts:
            if idx != 0:
                sb.append(", ")
            idx += 1
            sb.append(n.toDisplay())
        sb.append(")")
        return "".join(sb)

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNodeList(self.elts, v)

