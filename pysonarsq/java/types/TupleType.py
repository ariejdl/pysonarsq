#!/usr/bin/env python
""" generated source for module TupleType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from java.util import ArrayList

#from java.util import Collections

from java.util import List

from Type import Type


class TupleType(Type):
    """ generated source for class TupleType """

    #@overloaded
    def initsimple(self):
        from pysonarsq.java.Analyzer import Analyzer

        super(TupleType, self).__init__()
        self.eltTypes = ArrayList()
        self.getTable().addSuper(Analyzer.self.builtins.BaseTuple.getTable())
        self.getTable().setPath(Analyzer.self.builtins.BaseTuple.getTable().getPath())

    #@__init__.register(object, A)
    def __init__(self, *types):
        self.initsimple()
        
        if types != ():
            if len(types) == 1:
                if isinstance(types[0], list):
                    self.eltTypes += types[0]
            elif len(types):
                self.eltTypes += list(types)

    def setElementTypes(self, eltTypes):
        self.eltTypes = eltTypes

    def getElementTypes(self):
        return self.eltTypes

    def add(self, elt):
        self.eltTypes.append(elt)

    def get(self, i):
        return self.eltTypes[i]

    def toListType(self):
        from ListType import ListType

        t = ListType()
        for e in self.eltTypes:
            t.add(e)
        return t

    def __eq__(self, other):
        from pysonarsq.java._ import _
        
        if self.typeStack.contains(self, other):
            return True
        elif isinstance(other, (TupleType, )):
            types1 = self.getElementTypes();
            types2 = other.getElementTypes();
                        
            if len(types1) == len(types2):
                self.typeStack.push(self, other)
                i = 0
                while i < len(types1):
                    if not types1[i] == types2[i]:
                        self.typeStack.pop(self, other)
                        return False
                    i += 1
                self.typeStack.pop(self, other)
                return True
            else:
                return False
        else:
            return False

    def hashCode(self):
        return hash("TupleType")

    def printType(self, ctr):
        sb = []
        num = ctr.visit(self)
        if num is not None:
            sb.append("#")
            sb.append(num)
        else:
            newNum = ctr.push(self)
            first = True
            if len(self.getElementTypes()) != 1:
                sb.append("(")
            for t in self.getElementTypes():
                if not first:
                    sb.append(", ")
                sb.append(t.printType(ctr))
                first = False
            if ctr.isUsed(self):
                sb.append("=#")
                sb.append(newNum)
                sb.append(":")
            if len(self.getElementTypes()) != 1:
                sb.append(")")
            ctr.pop(self)
            
        return "".join(map(str, sb))

