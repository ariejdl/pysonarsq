
from org.jetbrains.annotations import NotNull


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from Node import Node

class Yield(Node):

    def __init__(self, n, start, end):
        super(Yield, self).__init__(start, end)
        self.value = n
        self.addChildren(n)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        if self.value is not None:
            return ListType(self.resolveExpr(self.value, s))
        else:
            return Analyzer.self.builtins.None_

    def __str__(self):
        return "<Yield:" + str(self.start) + ":" + str(self.value) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.value, v)

