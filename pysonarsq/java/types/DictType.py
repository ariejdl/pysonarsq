#!/usr/bin/env python
""" generated source for module DictType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull


from Type import Type


class DictType(Type):
    """ generated source for class DictType """


    #@__init__.register(object, Type, Type)
    def __init__(self, key0=None, val0=None):
        if key0 is None:
            key0 = Analyzer.self.builtins.unknown
        if val0 is None:
            val0 = Analyzer.self.builtins.unknown
        
        from pysonarsq.java.Analyzer import Analyzer

        super(DictType, self).__init__()
        self.keyType = key0
        self.valueType = val0
        self.getTable().addSuper(Analyzer.self.builtins.BaseDict.getTable())
        self.getTable().setPath(Analyzer.self.builtins.BaseDict.getTable().getPath())

    def add(self, key, val):
        """ generated source for method add """
        self.keyType = UnionType.union(self.keyType, key)
        self.valueType = UnionType.union(self.valueType, val)

    def toTupleType(self, n):
        ret = TupleType()
        i = 0
        while i < n:
            ret.add(self.keyType)
            i += 1
        return ret

    def __eq__(self, other):
        if self.typeStack.contains(self, other):
            return True
        elif isinstance(other, (DictType, )):
            self.typeStack.push(self, other)
            co = other;
            ret = (co.keyType == self.keyType) and (co.valueType == self.valueType)
            self.typeStack.pop(self, other)
            return ret
        else:
            return False

    def hashCode(self):
        return hash("DictType")

    def printType(self, ctr):
        sb = []
        num = ctr.visit(self)
        if num is not None:
            sb.append("#").append(num)
        else:
            ctr.push(self)
            sb.append("{")
            sb.append(self.keyType.printType(ctr))
            sb.append(" : ")
            sb.append(self.valueType.printType(ctr))
            sb.append("}")
            ctr.pop(self)
        return "".join(sb)

