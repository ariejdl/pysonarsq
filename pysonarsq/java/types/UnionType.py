#!/usr/bin/env python
""" generated source for module UnionType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

#from java.util import Collection

from java.util import HashSet

from java.util import Set

from Type import Type

class UnionType(Type):
    #types = Set()

    #@__init__.register(object, A)
    def __init__(self, *initialTypes):
        super(UnionType, self).__init__()
        self.types = HashSet()
        for nt in initialTypes:
            self.addType(nt)

    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.types.isEmpty()

    # 
    #      * Returns true if t1 == t2 or t1 is a union type that contains t2.
    #      
    @classmethod
    #@overloaded
    def contains(cls, t1, t2):
        
        if isinstance(t1, (UnionType, )):
            return t1._contains(t2)
        else:
            return t1 == t2
            
    def _contains(self, _type):
        return _type in self.types

    @classmethod
    def remove(cls, t1, t2):
        from pysonarsq.java.Analyzer import Analyzer

        if isinstance(t1, (UnionType, )):
            types = t1.getTypes().copy()
            if t2 in types: types.remove(t2)
            return UnionType.newUnion(types)
        elif t1 == t2:
            return Analyzer.self.builtins.unknown
        else:
            return t1

    @classmethod
    def newUnion(cls, types):
        from pysonarsq.java.Analyzer import Analyzer

        t = Analyzer.self.builtins.unknown
        for nt in types:
            t = cls.union(t, nt)
        return t

    def setTypes(self, types):
        self.types = types

    def getTypes(self):
        return self.types

    def addType(self, t):
        if t is None:
            return
        
        if t.isUnionType():
            self.types.update(t.asUnionType().types)
        else:
            self.types.add(t)

    #  take a union of two types
    #  with preference: other > None > Cont > unknown
    @classmethod
    def union(cls, u, v):
        from pysonarsq.java.Analyzer import Analyzer

        if u == v:
            return u
        elif u == Analyzer.self.builtins.unknown:
            return v
        elif v == Analyzer.self.builtins.unknown:
            return u
        elif u == Analyzer.self.builtins.None_:
            return v
        elif v == Analyzer.self.builtins.None_:
            return u
        else:
            return UnionType(u, v)

    # 
    #      * Returns the first alternate whose type is not unknown and
    #      * is not {@link org.yinwang.pysonar.Analyzer.idx.builtins.None}.
    #      *
    #      * @return the first non-unknown, non-{@code None} alternate, or {@code null} if none found
    #      
    def firstUseful(self):
        from pysonarsq.java.Analyzer import Analyzer        

        for type_ in self.types:
            if not type_.isUnknownType() and type_ != Analyzer.self.builtins.None_:
                return type_
        return None

    def __eq__(self, other):
        if self.typeStack.contains(self, other):
            return True
        elif isinstance(other, (UnionType, )):
            types1 = self.getTypes();
            types2 = other.getTypes();            
            
            if len(types1) != len(types2):
                return False
            else:
                self.typeStack.push(self, other)
                for t in types2:
                    if not t in types1:
                        self.typeStack.pop(self, other)
                        return False
                for t in types1:
                    if not t in types2:
                        self.typeStack.pop(self, other)
                        return False
                self.typeStack.pop(self, other)
                return True
        else:
            return False

    def hashCode(self):
        return hash("UnionType")

    def printType(self, ctr):
        sb = []
        num = ctr.visit(self)
        if num is not None:
            sb.append("#").append(num)
        else:
            newNum = ctr.push(self);
            first = True;
            sb.append("{")
            
            for t in self.types:
                if not first:
                    sb.append(" | ")
                sb.append(t.printType(ctr))
                first = False
            if ctr.isUsed(self):
                sb.append("=#").append(newNum).append(":")
            sb.append("}")
            ctr.pop(self)
        return "".join(sb)

