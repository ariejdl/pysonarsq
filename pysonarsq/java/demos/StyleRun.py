#!/usr/bin/env python
""" generated source for module StyleRun """
# package: org.yinwang.pysonar.demos
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from java.util import List

# 
#  * Represents a simple style run for purposes of source highlighting.
#  
#class StyleRun(Comparable, StyleRun):
class StyleRun(object):    
    """ generated source for class StyleRun """
    class Type:
        """ generated source for enum Type """
        KEYWORD = u'KEYWORD'
        COMMENT = u'COMMENT'
        STRING = u'STRING'
        DOC_STRING = u'DOC_STRING'
        IDENTIFIER = u'IDENTIFIER'
        BUILTIN = u'BUILTIN'
        NUMBER = u'NUMBER'
        CONSTANT = u'CONSTANT'
        FUNCTION = u'FUNCTION'
        PARAMETER = u'PARAMETER'
        LOCAL = u'LOCAL'
        DECORATOR = u'DECORATOR'
        CLASS = u'CLASS'
        ATTRIBUTE = u'ATTRIBUTE'
        LINK = u'LINK'
        ANCHOR = u'ANCHOR'
        DELIMITER = u'DELIMITER'
        TYPE_NAME = u'TYPE_NAME'
        ERROR = u'ERROR'
        WARNING = u'WARNING'
        INFO = u'INFO'

        #  ALL_CAPS identifier
        #  function name
        #  function parameter
        #  local variable
        #  function decorator
        #  class name
        #  object attribute
        #  hyperlink
        #  name anchor
        #  reference to a type (e.g. function or class name)

    #type_ = Type()
    #offset = int()

    #  file offset
    #length = int()

    #  style run length
    #message = str()

    #  optional hover text
    #url = str()

    #  internal or external link
    #id = str()

    #  for hover highlight
    #highlight = List()

    #  for hover highlight
    def __init__(self, type_, offset, length):
        super(StyleRun, self).__init__()
        
        self.type_ = type_
        self.offset = offset
        self.length = length
        self.message = None
        self.url = None
        self.id = None
        self.highlight = list()

    def start(self):
        """ generated source for method start """
        return self.offset

    def end(self):
        """ generated source for method end """
        return self.offset + self.length

    def length(self):
        """ generated source for method length """
        return self.length

    def __eq__(self, o):
        """ generated source for method equals """
        if not (isinstance(o, (StyleRun, ))):
            return False
        other = o
        return other.type_ == self.type_ and other.offset == self.offset and len(other) and equalFields(other.message, self.message) and equalFields(other.url, self.url)

    def equalFields(self, o1, o2):
        """ generated source for method equalFields """
        if o1 is None:
            return o2 is None
        else:
            return o1 == o2

    def compareTo(self, other):
        """ generated source for method compareTo """
        if self == other:
            return 0
        if self.offset < other.offset:
            return -1
        if other.offset < self.offset:
            return 1
        return self.hashCode() - other.hashCode()

    def __str__(self):
        """ generated source for method toString """
        return "[" + self.type_ + " beg=" + self.offset + " len=" + self.length + "]"

