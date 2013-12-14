#!/usr/bin/env python
""" generated source for module Attribute """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull
from org.jetbrains.annotations import Nullable

from pysonarsq.java.types.Type import Type
from pysonarsq.java.types.UnionType import UnionType

from java.util import List

from java.util import Set

from Node import Node
from Name import Name

class Attribute(Node):
    """ generated source for class Attribute """
    def __init__(self, target, attr, start, end):
        super(Attribute, self).__init__(start, end)
        
        self.target = target
        self.attr = attr
        self.addChildren(target, attr)

    def getAttributeName(self):
        """ generated source for method getAttributeName """
        return self.attr.id

    def getAttr(self):
        """ generated source for method getAttr """
        return self.attr

    def setAttr(self, s, v):
        """ generated source for method setAttr """
        targetType = self.resolveExpr(self.target, s)
        if targetType.isUnionType():
            for tp in types:
                self.setAttrType(tp, v)
        else:
            self.setAttrType(targetType, v)

    def setAttrType(self, targetType, v):

        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method setAttrType """
        if targetType.isUnknownType():
            Analyzer.self.putProblem(self, "Can't set attribute for UnknownType")
            return
        #  new attr, mark the type as "mutated"
        if targetType.getTable().lookupAttr(self.attr.id) is None or not targetType.getTable().lookupAttrType(self.attr.id) == v:
            targetType.setMutated(True)
            
        from pysonarsq.java.Binding import Binding
        ATTRIBUTE = Binding.Kind.ATTRIBUTE            
            
        targetType.getTable().insert(self.attr.id, self.attr, v, ATTRIBUTE)

    def resolve(self, s):
        targetType = self.resolveExpr(self.target, s)
        
        if targetType.isUnionType():
            from pysonarsq.java.Analyzer import Analyzer
            types = targetType.asUnionType().getTypes();
            retType = Analyzer.self.builtins.unknown;
            
            for tt in types:
                retType = UnionType.union(retType, self.getAttrType(tt))
            return retType
        else:
            return self.getAttrType(targetType)

    def getAttrType(self, targetType):
        from pysonarsq.java.Scope import Scope
        from pysonarsq.java.Analyzer import Analyzer

        bs = targetType.getTable().lookupAttr(self.attr.id)
        if bs is None:
            Analyzer.self.putProblem(self.attr, "attribute not found in type: " + str(targetType))
            t = Analyzer.self.builtins.unknown;
            t.getTable().setPath(targetType.getTable().extendPath(self.attr.id))
            return t
        else:
            for b in bs:
                Analyzer.self.putRef(self.attr, b)
                if self.getParent() is not None and self.getParent().isCall() and b.getType().isFuncType() and targetType.isInstanceType():
                    b.getType().asFuncType().setSelfType(targetType)
            
            return Scope.makeUnion(bs)

    def __str__(self):
        return "<Attribute:" + str(self.start) + ":" + str(self.target) + "." + str(self.getAttributeName()) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNode(self.target, v)
            self.visitNode(self.attr, v)

