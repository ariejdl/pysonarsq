#!/usr/bin/env python
""" generated source for module CallStack """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from pysonarsq.java.ast import *

from pysonarsq.java.types.Type import Type

from java.util import HashSet

from java.util import Set

class CallStack(object):
    """ generated source for class CallStack """
    stack = HashSet()

    def push(self, call, type_):
        """ generated source for method push """
        self.stack.add(call)

    def pop(self, call, type_):
        """ generated source for method pop """
        self.stack.remove(call)

    def contains(self, call, type_):
        """ generated source for method contains """
        return self.stack.contains(call)

