#!/usr/bin/env python
""" generated source for module TypeStack """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from java.util import ArrayList

from java.util import List

class TypeStack(object):
    class Pair(object):
        def __init__(self, first, second):
            self.first = first
            self.second = second

    def __init__(self):
        self.stack = ArrayList()

    def push(self, first, second):
        self.stack.append(self.Pair(first, second))

    def pop(self, first, second):
        if len(self.stack):
            self.stack.pop()
        #v = len(self.stack) - 1
        #if v in self.stack: self.stack.remove(v)

    def contains(self, first, second):
        for p in self.stack:
            if (p.first is first and p.second is second) or (p.first is second and p.second is first):
                return True
        return False

