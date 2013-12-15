#!/usr/bin/env python
""" generated source for module Dict """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.DictType import DictType

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Dict(Node):

    def __init__(self, keys, values, start, end):
        super(Dict, self).__init__(start, end)
        self.keys = keys
        self.values = values
        self.addChildren(keys)
        self.addChildren(values)

    def resolve(self, s):
        keyType = self.resolveListAsUnion(self.keys, s)
        valType = self.resolveListAsUnion(self.values, s)
        return DictType(keyType, valType)

    def __str__(self):
        return "<Dict>"

    def visit(self, v):
        if v.visit(self):
            #  XXX:  should visit in alternating order
            self.visitNodeList(self.keys, v)
            self.visitNodeList(self.values, v)

