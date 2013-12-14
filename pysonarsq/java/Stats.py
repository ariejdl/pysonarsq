#!/usr/bin/env python
""" generated source for module Stats """
# package: org.yinwang.pysonar
from java.util import HashMap

from java.util import Map

class Stats(object):
    """ generated source for class Stats """
    contents = HashMap()

    def putInt(self, key, value):
        """ generated source for method putInt """
        self.contents[key] = value

    #@overloaded
    def inc(self, key, x=None):
        """ generated source for method inc """
        if x is None: x = 1
        old = self.getInt(key)
        if old is None:
            self.contents[key] = 1
        else:
            self.contents[key] = old + x

    def getInt(self, key):
        """ generated source for method getInt """
        ret = long(self.contents.get(key, 0))
        if ret is None:
            return 0
        else:
            return ret

    def print_(self):
        """ generated source for method print_ """
        sb = []
        for e in contents.items():
            sb.append("\n- " + e[0] + ": " + e[1])
        return "".join(sb)

