#!/usr/bin/env python
""" generated source for module Subscript """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull


#from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType
from pysonarsq.java.types.ListType import ListType

from Node import Node

class Subscript(Node):

    #  an NIndex or NSlice
    def __init__(self, value, slice_, start, end):
        super(Subscript, self).__init__(start, end)
        self.value = value
        self.slice_ = slice_
        self.addChildren(value, slice_)

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        
        vt = self.resolveExpr(self.value, s)
        st = self.resolveExpr(self.slice_, s)
        if vt.isUnionType():
            for t in vt.asUnionType().getTypes():
                retType = Analyzer.self.builtins.unknown;
                retType = UnionType.union(retType, self.getSubscript(t, st, s))
            return retType
        else:
            return self.getSubscript(vt, st, s)

    def getSubscript(self, vt, st, s):
        from pysonarsq.java.Analyzer import Analyzer

        if vt.isUnknownType():
            return Analyzer.self.builtins.unknown
        elif vt.isListType():
            return self.getListSubscript(vt, st, s)
        elif vt.isTupleType():
            return self.getListSubscript(vt.asTupleType().toListType(), st, s)
        elif vt.isDictType():
            nl = ListType(vt.asDictType().valueType);
            return self.getListSubscript(nl, st, s)
        elif vt.isStrType():
            if st.isListType() or st.isNumType():
                return vt
            else:
                self.addWarning("Possible KeyError (wrong type for subscript)")
                return Analyzer.self.builtins.unknown
        else:
            return Analyzer.self.builtins.unknown

    def getListSubscript(self, vt, st, s):
        from pysonarsq.java.Analyzer import Analyzer

        if vt.isListType():
            if st.isListType():
                return vt
            elif st.isNumType():
                return vt.asListType().getElementType()
            else:
                sliceFunc = vt.getTable().lookupAttrType("__getslice__");
                if sliceFunc is None:
                    self.addError("The type can't be sliced: " + vt)
                    return Analyzer.self.builtins.unknown
                elif sliceFunc.isFuncType():
                    from Call import Call
                    return Call.apply(sliceFunc.asFuncType(), None, None, None, None, self)
                else:
                    self.addError("The type's __getslice__ method is not a function: " + sliceFunc)
                    return Analyzer.self.builtins.unknown
        else:
            return Analyzer.self.builtins.unknown

    def __str__(self):
        return "<Subscript:" + str(self.value) + ":" + str(self.slice_) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.value, v)
            self.visitNode(self.slice_, v)

