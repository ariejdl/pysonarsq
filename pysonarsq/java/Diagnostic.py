#!/usr/bin/env python
""" generated source for module Diagnostic """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

class Diagnostic(object):
    """ generated source for class Diagnostic """
    class Category:
        """ generated source for enum Category """
        INFO = u'INFO'
        WARNING = u'WARNING'
        ERROR = u'ERROR'

    file_ = str()
    category = Category()
    start = int()
    end = int()
    msg = str()

    def __init__(self, file_, category, start, end, msg):
        """ generated source for method __init__ """
        self.category = category
        self.file_ = file_
        self.start = start
        self.end = end
        self.msg = msg

    def __str__(self):
        """ generated source for method toString """
        return "<Diagnostic:" + self.file_ + ":" + self.category + ":" + self.msg + ">"

