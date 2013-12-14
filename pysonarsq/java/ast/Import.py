#!/usr/bin/env python
""" generated source for module Import """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Binding import Binding

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ModuleType import ModuleType

from pysonarsq.java.types.Type import Type

from java.util import List

from Node import Node

class Import(Node):

    def __init__(self, names, start, end):
        super(Import, self).__init__(start, end)
        self.names = names
        self.addChildren(names)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        for a in self.names:
            mod = Analyzer.self.loadModule(a.name, s);
            if mod is None:
                Analyzer.self.putProblem(self, "Cannot load module")
            elif a.asname is not None:
                s.insert(a.asname.id, a.asname, mod, Binding.Kind.VARIABLE)
        return Analyzer.self.builtins.Cont

    def __str__(self):
        return "<Import:" + str(self.names) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.names, v)

