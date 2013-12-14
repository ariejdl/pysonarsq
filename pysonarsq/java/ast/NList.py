
from org.jetbrains.annotations import NotNull

from pysonarsq.java.types.ListType import ListType
from pysonarsq.java.types.Type import Type
from pysonarsq.java.types.UnionType import UnionType

from java.util import List

from Str import Str
from Sequence import Sequence

class NList(Sequence):

    def __init__(self, elts, start, end):
        super(NList, self).__init__(elts, start, end)

    def resolve(self, s):
        if len(self.elts) == 0:
            return ListType()
            #  list<unknown>
        listType = ListType()
        for elt in self.elts:
            listType.add(self.resolveExpr(elt, s))
            if isinstance(elt, (Str, )):
                listType.addValue((elt).getStr())
        return listType

    def __str__(self):
        """ generated source for method toString """
        return "<List:" + str(self.start) + ":" + str(self.elts) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNodeList(self.elts, v)

