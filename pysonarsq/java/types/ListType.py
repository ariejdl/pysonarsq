#!/usr/bin/env python
""" generated source for module ListType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from java.util import ArrayList

from java.util import List

from Type import Type
from UnionType import UnionType
from TupleType import TupleType

class ListType(Type):
    """ generated source for class ListType """


    #@__init__.register(object, Type)
    def __init__(self, elt0=None):
        self.positional = list()
        self.values = list()
        
        from pysonarsq.java.Analyzer import Analyzer
        
        super(ListType, self).__init__()
        self.eltType = elt0
        self.getTable().addSuper(Analyzer.self.builtins.BaseList.getTable())
        self.getTable().setPath(Analyzer.self.builtins.BaseList.getTable().getPath())
        
        if self.eltType is None:
            self.eltType = Analyzer.self.builtins.unknown

    def setElementType(self, eltType):
        self.eltType = eltType

    def getElementType(self):
        return self.eltType

    def add(self, another):
        self.eltType = UnionType.union(self.eltType, another)
        self.positional.append(another)

    def addValue(self, v):
        self.values.append(v)

    def get(self, i):
        return self.positional[i]

    #@overloaded
    def toTupleType(self, n=None):
        if n is None:
            return TupleType(*self.positional)

        ret = TupleType()
        for i in range(n):
            ret.add(self.eltType)
        return ret

    def __eq__(self, other):

        if self.typeStack.contains(self, other):
            return True
        elif isinstance(other, (ListType, )):
            co = other;
            self.typeStack.push(self, other)
            ret = co.getElementType() == self.getElementType();
            self.typeStack.pop(self, other)
            return ret
        else:
            return False
            

    def hashCode(self):
        return hash("ListType")

    def printType(self, ctr):
        sb = []
        num = ctr.visit(self)
        if num is not None:
            sb.append("#")
            sb.append(num)
        else:
            ctr.push(self)
            sb.append("[")
            sb.append(self.getElementType().printType(ctr))
            sb.append("]")
            ctr.pop(self)
            
        return "".join(map(str, sb)).encode('utf-8')

