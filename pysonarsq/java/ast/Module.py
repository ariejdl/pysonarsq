#!/usr/bin/env python
""" generated source for module Module """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java._ import _

from pysonarsq.java.types.ModuleType import ModuleType

from pysonarsq.java.types.Type import Type

from java.io import File

from Node import Node
from Block import Block

import os

class Module(Node):
    """ generated source for class Module """

    #  input source file sha1
    def __init__(self, body, start, end):
        """ generated source for method __init__ """
        super(Module, self).__init__(start, end)
        self.body = body
        self.addChildren(self.body)

    #@overloaded
    def setFile(self, file_):
        if os.sep not in file_:
            file_ = os.path.abspath(file_)
        
        self.file_ = file_
        self.name = _.moduleName(file_)
        self.sha1 = _.getSHA1(File(file_))

    def getFile(self):
        """ generated source for method getFile """
        return self.file_

    def getSHA1(self):
        """ generated source for method getSHA1 """
        return self.sha1

    def resolve(self, s):
        from pysonarsq.java.Binding import Binding
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        mt = ModuleType(self.name, self.file_, Analyzer.self.globaltable)
        s.insert(_.moduleQname(self.file_), self, mt, Binding.Kind.MODULE)
        self.resolveExpr(self.body, mt.getTable())
        return mt

    def __str__(self):
        """ generated source for method toString """
        return "<Module:" + self.file_ + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.body, v)

