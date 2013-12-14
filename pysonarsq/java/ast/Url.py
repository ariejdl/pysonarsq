#!/usr/bin/env python
""" generated source for module Url """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


#from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node

# 
#  * virtual-AST node used to represent virtual source locations for builtins
#  * as external urls.
#  
class Url(Node):
    """ generated source for class Url """

    def __init__(self, url):
        """ generated source for method __init__ """
        super(Url, self).__init__()
        self.url = url

    def getURL(self):
        """ generated source for method getURL """
        return self.url

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.BaseStr

    def __str__(self):
        """ generated source for method toString """
        return "<Url:\"" + self.url + "\">"

    def visit(self, v):
        """ generated source for method visit """
        v.visit(self)

    def startswith(self, w):
        return self.url.startswith(w)
