#!/usr/bin/env python
""" generated source for module HtmlOutline """
# package: org.yinwang.pysonar.demos
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.Analyzer import Analyzer

from pysonarsq.java.Outliner import Outliner
from pysonarsq.java._ import _

from java.util import List

from pysonarsq.java.Binding import Binding
ATTRIBUTE = Binding.Kind.ATTRIBUTE
CLASS = Binding.Kind.CLASS
CONSTRUCTOR = Binding.Kind.CONSTRUCTOR
FUNCTION = Binding.Kind.FUNCTION
METHOD = Binding.Kind.METHOD
MODULE = Binding.Kind.MODULE
PARAMETER = Binding.Kind.PARAMETER
SCOPE = Binding.Kind.SCOPE
VARIABLE = Binding.Kind.VARIABLE

class HtmlOutline(object):

    def __init__(self, idx):
        self.analyzer = idx
        self.buffer_ = []

    def generate(self, path):
        self.buffer_ = []
        entries = self.generateOutline(self.analyzer, path)
        self.addOutline(entries)
        html = ''.join(self.buffer_)
        self.buffer_ = None
        return html

    def generateOutline(self, analyzer, file_):
        return Outliner().generate(analyzer, file_)

    def addOutline(self, entries):
        self.add("<ul>\n")
        for e in entries:
            self.addEntry(e)
        self.add("</ul>\n")

    def addEntry(self, e):
        self.add("<li>")
        style = None
        
        if e.getKind()==FUNCTION or e.getKind()==METHOD or e.getKind()==CONSTRUCTOR:
            style = "function"
        elif e.getKind()==CLASS:
            style = "type-name"
        elif e.getKind()==PARAMETER:
            style = "parameter"
        elif e.getKind()==VARIABLE or e.getKind()==SCOPE:
            style = "identifier"
            
        self.add('<a href="#')
        self.add(e.getQname())
        self.add('" onmouseover="highlight(\'' + _.escapeQname(e.getQname()) + '\')">')
        
        if style is not None:
            self.add('<span class="')
            self.add(style)
            self.add('">')
            
        self.add(e.getName())
        
        if style is not None:
            self.add("</span>")
            
        self.add("</a>")
        
        if e.isBranch():
            self.addOutline(e.getChildren())
            
        self.add("</li>")

    def add(self, text):
        """ generated source for method add """
        self.buffer_.append(text)

