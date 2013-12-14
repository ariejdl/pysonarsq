#!/usr/bin/env python
""" generated source for module Block """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from java.util import List

from Node import Node

class Block(Node):

    def __init__(self, seq, start, end):
        super(Block, self).__init__(start, end)
        self.seq = seq
        self.addChildren(seq)

    def resolve(self, scope):
        
        from pysonarsq.java.Analyzer import Analyzer   
        from pysonarsq.java.Scope import Scope     

        #  find global names and mark them
        for n in self.seq:
            if n.isGlobal():
                for name in n.asGlobal().getNames():
                    scope.addGlobalName(name.id)
                    nb = scope.lookup(name.id);
                    if nb is not None:
                        Analyzer.self.putRef(name, nb)
                        
        returned = False
        retType = Analyzer.self.builtins.unknown
        
        for n in self.seq:
            t = self.resolveExpr(n, scope);
            
            if not returned:
                retType = UnionType.union(retType, t)
                if not UnionType.contains(t, Analyzer.self.builtins.Cont):
                    returned = True
                    retType = UnionType.remove(retType, Analyzer.self.builtins.Cont)
            elif scope.getScopeType() != Scope.ScopeType.GLOBAL and scope.getScopeType() != Scope.ScopeType.MODULE:
                Analyzer.self.putProblem(n, "unreachable code")
        
        return retType

    def isEmpty(self):
        return len(self.seq) == 0

    def __str__(self):
        return "<Block:" + str(self.seq) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.seq, v)

