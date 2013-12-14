#!/usr/bin/env python
""" generated source for module DictComp """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.DictType import DictType

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class DictComp(Node):
    """ generated source for class DictComp """

    def __init__(self, key, value, generators, start, end):
        """ generated source for method __init__ """
        super(DictComp, self).__init__(start, end)
        self.key = key
        self.value = value
        self.generators = generators
        self.addChildren(key)
        self.addChildren(generators)

    # 
    #      * Python's list comprehension will bind the variables used in generators.
    #      * This will erase the original values of the variables even after the
    #      * comprehension.
    #      
    def resolve(self, s):
        """ generated source for method resolve """
        resolveList(self.generators, s)
        keyType = resolveExpr(self.key, s)
        valueType = resolveExpr(self.value, s)
        return DictType(keyType, valueType)

    def __str__(self):
        """ generated source for method toString """
        return "<DictComp:" + start + ":" + self.key + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.key, v)
            self.visitNodeList(self.generators, v)

