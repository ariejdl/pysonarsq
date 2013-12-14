#!/usr/bin/env python
""" generated source for module Type """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.TypeStack import TypeStack

from pysonarsq.java._ import _

from java.util import HashMap

from java.util import HashSet

from java.util import Map

from java.util import Set

class Type(object):

    def __init__(self):
        self.mutated = False
        self.typeStack = TypeStack()
        self.table = None

    def setTable(self, table):
        self.table = table

    def getTable(self):
        from pysonarsq.java.Scope import Scope

        if self.table is None:
            self.table = Scope(None, Scope.ScopeType.SCOPE)
        return self.table

    def isMutated(self):
        return self.mutated

    def setMutated(self, mutated):
        self.mutated = mutated

    # 
    #      * Returns {@code true} if this Python type is implemented in native code
    #      * (i.e., C, Java, C# or some other host language.)
    #      
    def isNative(self):
        from pysonarsq.java.Analyzer import Analyzer
        return Analyzer.self.builtins.isNative(self)

    def isClassType(self):
        from ClassType import ClassType
        return isinstance(self, (ClassType, ))

    def isDictType(self):
        from DictType import DictType
        return isinstance(self, (DictType, ))

    def isFuncType(self):
        from FunType import FunType
        return isinstance(self, (FunType, ))

    def isInstanceType(self):
        from InstanceType import InstanceType
        return isinstance(self, (InstanceType, ))

    def isListType(self):
        from ListType import ListType
        return isinstance(self, (ListType, ))

    def isModuleType(self):
        from ModuleType import ModuleType
        return isinstance(self, (ModuleType, ))

    def isNumType(self):
        from pysonarsq.java.Analyzer import Analyzer
        return (self == Analyzer.self.builtins.BaseNum or self == Analyzer.self.builtins.BaseFloat or self == Analyzer.self.builtins.BaseComplex)

    def isStrType(self):
        from pysonarsq.java.Analyzer import Analyzer
        return self == Analyzer.self.builtins.BaseStr

    def isTupleType(self):
        from TupleType import TupleType
        return isinstance(self, (TupleType, ))

    def isUnionType(self):
        from UnionType import UnionType
        return isinstance(self, (UnionType, ))

    def isUnknownType(self):
        from pysonarsq.java.Analyzer import Analyzer
        return self == Analyzer.self.builtins.unknown

    def asClassType(self):
        return self

    def asDictType(self):
        return self

    def asFuncType(self):
        return self

    def asInstanceType(self):
        return self

    def asListType(self):
        return self

    def asModuleType(self):
        if self.isUnionType():
            for t in self.asUnionType().getTypes():
                if t.isModuleType():
                    return t.asModuleType()
            _.die("Not containing a ModuleType")
            return ModuleType(None, None, None)
        elif self.isModuleType():
            return self
        else:
            _.die("Not a ModuleType")
            return ModuleType(None, None, None)

    def asTupleType(self):
        return self

    def asUnionType(self):
        return self

    class CyclicTypeRecorder(object):

        def __init__(self):
            self.count = 0
            self.elements = HashMap()
            self.used = HashSet()

        def push(self, t):
            self.count += 1
            self.elements[t] = self.count
            return self.count

        def pop(self, t):
            del self.elements[t]
            if t in self.used:
                self.used.remove(t)

        def visit(self, t):
            i = self.elements.get(t)
            if i is not None:
                self.used.add(t)
            return i

        def isUsed(self, t):
            return t in self.used

    def printType(self, ctr):
        raise Exception('abstract')

    def __str__(self):
        return self.printType(Type.CyclicTypeRecorder())
    
    def __eq__(self, o):
        return self is o
        
    def __cmp__(self, o):
        return 0 if self == 1 else self.__hash__() - o.__hash__()
        
    def __hash__(self):
        return self.hashCode()

