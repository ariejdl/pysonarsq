#!/usr/bin/env python
""" generated source for module ModuleType """
# package: org.yinwang.pysonar.types
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable


from pysonarsq.java._ import _

from Type import Type


class ModuleType(Type):
    """ generated source for class ModuleType """
    file_ = str()
    name = str()
    qname = str()

    def __init__(self, name=None, file_=None, parent=None):
        from pysonarsq.java.Scope import Scope
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method __init__ """
        super(ModuleType, self).__init__()
        self.name = name
        self.file_ = file_
        #  null for builtin modules
        if file_ is not None:
            #  This will return null iff specified file is not prefixed by
            #  any path in the module search path -- i.e., the caller asked
            #  the analyzer to load a file not in the search path.
            self.qname = _.moduleQname(file_)
        if self.qname is None:
            self.qname = name
        self.setTable(Scope(parent, Scope.ScopeType.MODULE))
        self.getTable().setPath(self.qname)
        self.getTable().setType(self)
        #  null during bootstrapping of built-in types
        if Analyzer.self.builtins is not None:
            self.getTable().addSuper(Analyzer.self.builtins.BaseModule.getTable())

    def setFile(self, file_):
        self.file_ = file_

    def getFile(self):
        return self.file_

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getQname(self):
        return self.qname

    def hashCode(self):
        return hash("ModuleType")

    def __eq__(self, other):
        if isinstance(other, (ModuleType, )):
            co = other;
            if self.file_ is not None:
                return self.file_ == co.file_
        return self is other

    def printType(self, ctr):
        return self.getName()

