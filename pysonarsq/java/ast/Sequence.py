#!/usr/bin/env python
""" generated source for module Sequence """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from java.util import List

from Node import Node

class Sequence(Node):
    """ generated source for class Sequence """

    def __init__(self, elts, start, end):
        super(Sequence, self).__init__(start, end)
        self.elts = elts
        self.addChildren(elts)

