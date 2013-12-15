#!/usr/bin/env python
""" generated source for module ImportFrom """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable


from pysonarsq.java.Binding import Binding

from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.ModuleType import ModuleType

from pysonarsq.java.types.Type import Type

from java.util import ArrayList

from java.util import List

from Node import Node

#(from java.util import Map.Entry)

class ImportFrom(Node):

    def __init__(self, module_, names, level, start, end):
        super(ImportFrom, self).__init__(start, end)
        self.module_ = module_
        self.level = level
        self.names = names
        self.addChildren(names)

    def bindsName(self):
        return True

    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer

        if self.module_ is None:
            return Analyzer.self.builtins.Cont
        mod = Analyzer.self.loadModule(self.module_, s)
        if mod is None:
            Analyzer.self.putProblem(self, "Cannot load module")
        elif self.isImportStar():
            self.importStar(s, mod)
        else:
            for a in self.names:
                first = a.name[0];
                bs = mod.getTable().lookup(first.id)
                if bs is not None:
                    if a.asname is not None:
                        s.update(a.asname.id, bs)
                        Analyzer.self.putRef(a.asname, bs)
                    else:
                        s.update(first.id, bs)
                        Analyzer.self.putRef(first, bs)
                else:
                    ext = list(self.module_);
                    ext.append(first)
                    mod2 = Analyzer.self.loadModule(ext, s);
                    if mod2 is not None:
                        if a.asname is not None:
                            s.insert(a.asname.id, a.asname, mod2, Binding.Kind.VARIABLE)
                        else:
                            s.insert(first.id, first, mod2, Binding.Kind.VARIABLE)
        return Analyzer.self.builtins.Cont

    def isImportStar(self):
        return len(self.names) == 1 and "*" == self.names[0].name[0].id

    def importStar(self, s, mt):
        from pysonarsq.java.Analyzer import Analyzer

        if mt is None or mt.getFile() is None:
            return
        mod = Analyzer.self.getAstForFile(mt.getFile())
        if mod is None:
            return
        names = ArrayList()
        allType = mt.getTable().lookupType("__all__")
        if allType is not None and allType.isListType():
            lt = allType.asListType();
            for o in lt.values:
                if isinstance(o, (str, )):
                    names.append(str(o))
        if len(names):
            for name in names:
                b = mt.getTable().lookupLocal(name);
                if b is not None:
                    s.update(name, b)
                else:
                    m2 = list()
                    m2.append(Name(name))
                    mod2 = Analyzer.self.loadModule(m2, s);
                    if mod2 is not None:
                        s.insert(name, None, mod2, Binding.Kind.VARIABLE)
        else:
            for e in mt.getTable().entrySet():
                if not e[0].startswith("_"):
                    s.update(e[0], e[1])

    def __str__(self):
        return "<FromImport:" + str(self.module_) + ":" + str(self.names) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.names, v)

