#!/usr/bin/env python
""" generated source for module Styler """
# package: org.yinwang.pysonar.demos
from org.jetbrains.annotations import NotNull

from pysonarsq.java.Analyzer import Analyzer

from pysonarsq.java.ast.DefaultNodeVisitor import DefaultNodeVisitor
from pysonarsq.java.ast.FunctionDef import FunctionDef
from pysonarsq.java.ast.Num import Num
from pysonarsq.java.ast.Str import Str
from pysonarsq.java.ast.Name import Name

from java.util import ArrayList
from java.util import HashSet
from java.util import List
from java.util import Set

import re
import math

from StyleRun import StyleRun

# 
#  * Decorates Python source with style runs from the index.
#  
class Styler(DefaultNodeVisitor):
    """ generated source for class Styler """
    BUILTIN = re.compile("None|True|False|NotImplemented|Ellipsis|__debug__")

    # 
    #      * Matches the start of a triple-quote string.
    #      
    TRISTRING_PREFIX = re.compile("^[ruRU]{0,2}['\"]{3}")
    #linker = Linker()

    # 
    #      * Offsets of doc strings found by node visitor.
    #      
    docOffsets = HashSet()

    def __init__(self, idx, linker):
        """ generated source for method __init__ """
        super(Styler, self).__init__()
        self.analyzer = idx
        self.styles = ArrayList()
        self.linker = linker
        self.path = None
        self.source = None
        

    # 
    #      * Entry point for decorating a source file.
    #      *
    #      * @param path absolute file path
    #      * @param src  file contents
    #      
    def addStyles(self, path, src):
        """ generated source for method addStyles """
        self.path = path
        self.source = src
        m = self.analyzer.getAstForFile(path)
        if m is not None:
            m.visit(self)
        
        self.styles = sorted(self.styles, lambda a,b: a.compareTo(b))
        return self.styles

    #@overloaded
    def visit(self, n):
        if isinstance(n, Num):
            self.addStyle(n, StyleRun.Type.NUMBER)
            return True
            
        if isinstance(n, Str):
            s = self.sourceString(n.start, n.end)
            #if self.TRISTRING_PREFIX.match(s).lookingAt():
            if self.TRISTRING_PREFIX.match(s) is not None:
                self.addStyle(n.start, n.end - n.start, StyleRun.Type.DOC_STRING)
                self.docOffsets.add(n.start)
            #  don't re-highlight as a string
            #             highlightDocString(n);
            return True            

        if isinstance(n, Name):
            parent = n.getParent()
            if isinstance(parent, (FunctionDef, )):
                fn = parent;
                if n == fn.name:
                    self.addStyle(n, StyleRun.Type.FUNCTION)
                elif n == fn.kwarg or n == fn.vararg:
                    self.addStyle(n, StyleRun.Type.PARAMETER)
                return True
            if self.BUILTIN.match(n.id) is not None:
                self.addStyle(n, StyleRun.Type.BUILTIN)
                return True
                
        return True
        
    def addStyle(self, *args):
        if len(args) == 4:
            self.addStyle1(*args)
        elif len(args) == 2:
            self.addStyle2(*args)
        elif len(args) == 3:
            self.addStyle3(*args)

    #@overloaded
    def addStyle1(self, e, start, len, type_):
        if e.getFile() is not None:
            #  if it's an NUrl, for instance
            self.addStyle(start, len, type_)

    #@addStyle.register(object, Node, StyleRun.Type)
    def addStyle2(self, e, type_):
        self.addStyle(e, e.start, e.end - e.start, type_)

    #@addStyle.register(object, int, int, StyleRun.Type)
    def addStyle3(self, begin, len, type_):
        self.styles.append(StyleRun(type_, begin, len))
        
    def sourceString(self, *args):        
        if len(args) == 1:
            return self.sourceString0(*args)
        else:
            return self.sourceString1(*args)

    #@overloaded
    def sourceString0(self, e):
        """ generated source for method sourceString """
        return self.sourceString(e.start, e.end)

    #@sourceString.register(object, int, int)
    def sourceString1(self, begin, end):
        """ generated source for method sourceString_0 """
        a = max(begin, 0)
        b = min(end, len(self.source))
        b = max(b, 0)
        try:
            return self.source[a, b]
        except Exception as sx:
            #  Silent here, only happens for weird encodings in file
            return ""

