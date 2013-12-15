#!/usr/bin/env python
""" generated source for module StyleApplier """
# package: org.yinwang.pysonar.demos
from org.jetbrains.annotations import NotNull

from pysonarsq.java._ import _

from java.util import List

from java.util import TreeSet
from StyleRun import StyleRun


KEYWORD = StyleRun.Type.KEYWORD
COMMENT = StyleRun.Type.COMMENT
STRING = StyleRun.Type.STRING
DOC_STRING = StyleRun.Type.DOC_STRING
IDENTIFIER = StyleRun.Type.IDENTIFIER
BUILTIN = StyleRun.Type.BUILTIN
NUMBER = StyleRun.Type.NUMBER
CONSTANT = StyleRun.Type.CONSTANT
FUNCTION = StyleRun.Type.FUNCTION
PARAMETER = StyleRun.Type.PARAMETER
LOCAL = StyleRun.Type.LOCAL
DECORATOR = StyleRun.Type.DECORATOR
CLASS = StyleRun.Type.CLASS
ATTRIBUTE = StyleRun.Type.ATTRIBUTE
LINK = StyleRun.Type.LINK
ANCHOR = StyleRun.Type.ANCHOR
DELIMITER = StyleRun.Type.DELIMITER
TYPE_NAME = StyleRun.Type.TYPE_NAME
ERROR = StyleRun.Type.ERROR
WARNING = StyleRun.Type.WARNING
INFO = StyleRun.Type.INFO

# 
#  * Turns a list of {@link StyleRun}s into HTML spans.
#  
class StyleApplier(object):
    """ generated source for class StyleApplier """
    #  Empirically, adding the span tags multiplies length by 6 or more.
    SOURCE_BUF_MULTIPLIER = 6

#    class Tag(Comparable, Tag):
    class Tag(object):        
        """ generated source for class Tag """
        def __init__(self):
            pass
        
        def compareTo(self, other):
            return self.__cmp__(other)
            
        def __cmp__(self, other):
            if self is other: return 0
            if self.offset < other.offset: return -1
            if other.offset < self.offset: return 1
            #return self.offset - other.offset
            return hash(self) - hash(other)
        
        """
        def __eq__(self, other): return self is other
        def __ne__(self, other): return self is not other
        def __lt__(self, other): return self.offset < other.offset
        def __le__(self, other): return self.offset <= other.offset
        def __gt__(self, other): return self.offset > other.offset
        def __ge__(self, other): return self.offset >= other.offset
        """        

        def insert(self):
            #  Copy source code up through this tag.
            if self.offset > self.applier.sourceOffset:
                self.applier.copySource(self.applier.sourceOffset, self.offset)

    class StartTag(Tag):

        def __init__(self, style, applier):
            super(StyleApplier.StartTag, self).__init__()
            
            self.applier = applier
            self.offset = style.start()
            self.style = style

        def insert(self):
            super(StyleApplier.StartTag, self).insert()
            
            if self.style.type_==ANCHOR:
                self.applier.buffer_.append('<a name="' + self.style.url + '" ')
                self.applier.buffer_.append('id="' + self.style.id + '"')
                if self.style.highlight is not None and len(self.style.highlight) > 0:
                    ids = _.joinWithSep(self.style.highlight, "\',\'", "\'", "\'");
                    self.applier.buffer_.append('onmouseover="highlight(')
                    self.applier.buffer_.append(ids)
                    self.applier.buffer_.append(')" ')
                    
            elif self.style.type_==LINK:
                self.applier.buffer_.append('<a href="' + self.style.url + '"')
                self.applier.buffer_.append(' id="' + self.style.id + '"')
                if self.style.highlight is not None and len(self.style.highlight) > 0:
                    ids = _.joinWithSep(self.style.highlight, "\',\'", "\'", "\'");
                    self.applier.buffer_.append('onmouseover="highlight(')
                    self.applier.buffer_.append(ids)
                    self.applier.buffer_.append(')" ')
                    
            else:
                self.applier.buffer_.append('<span class="')
                self.applier.buffer_.append(self.applier.toCSS(self.style))
                self.applier.buffer_.append('" ')
                
            if self.style.message is not None:
                self.applier.buffer_.append(' title="')
                self.applier.buffer_.append(self.style.message)
                self.applier.buffer_.append('" ')
                
            self.applier.buffer_.append(">")

    class EndTag(Tag):

        def __init__(self, style, applier):
            super(StyleApplier.EndTag, self).__init__()

            self.applier = applier
            self.offset = style.end()
            self.style = style

        def insert(self):
            super(StyleApplier.EndTag, self).insert()
            
            if self.style.type_==ANCHOR or self.style.type_==LINK:
                self.applier.buffer_.append("</a>")
            else:
                self.applier.buffer_.append("</span>")

    def __init__(self, path, src, runs):
        self.tags = TreeSet()
        self.buffer_ = []
        self.sourceOffset = 0        
        self.source = src
        
        for run in runs:
            self.tags.add(StyleApplier.StartTag(run, self))
            self.tags.add(StyleApplier.EndTag(run, self))

    def apply(self):
        def sortFn(a,b):
            return a.compareTo(b)
        
        self.buffer_ = []
        self.tags = sorted(self.tags, sortFn)
        
        for tag in self.tags:
            tag.insert()
            
        if self.sourceOffset < len(self.source):
            self.copySource(self.sourceOffset, len(self.source))
            
        return u''.join(map(lambda s: s.encode('utf-8'), self.buffer_))

    def copySource(self, begin, end):
        inner = self.source[0:begin] if (end == -1) else self.source[begin:end]
        src = self.escape(inner);
        self.buffer_.append(src)
        self.sourceOffset = end

    def escape(self, s):
        return s.replace("&", "&amp;").replace("'", "&#39;").replace("\"", "&quot;").replace("<", "&lt;").replace(">", "&gt;")

    def toCSS(self, style):
        return style.type_.__str__().lower().replace("_", "-")

