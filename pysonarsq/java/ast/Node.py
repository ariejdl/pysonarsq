#!/usr/bin/env python

# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

#from pysonarsq.java.Analyzer import Analyzer

#from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from java.util import ArrayList

from java.util import List

#class Node(java.io.Serializable):
class Node(object):    
    #@__init__.register(object, int, int)
    def __init__(self, start=-1, end=-1):
        self.start = start
        self.end = end
        
        if not hasattr(self, 'parent'):
            self.parent = None

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def getAstRoot(self):
        if self.parent is None:
            return self
        return self.parent.getAstRoot()

    def length(self):
        return self.end - self.start

    def bindsName(self):
        return False

    def getFile(self):
        return self.parent.getFile() if self.parent is not None else None

    #@overloaded
    def addChildren(self, *args):
        if args is None:
            return
            
        nodes = []
        if len(args):
            if isinstance(args[0], list):
                nodes = args[0]
            else:
                nodes = args
            
        if nodes is not None:
            for n in nodes:
                if n is not None:
                    n.setParent(self)

    def getDocString(self):
        body = None
        if isinstance(self, (FunctionDef, )):
            body = (self).body
        elif isinstance(self, (ClassDef, )):
            body = (self).body
        elif isinstance(self, (Module, )):
            body = (self).body
        if isinstance(body, (Block, )) and len(body.seq) >= 1:
            if isinstance(firstExpr, (Expr, )):
                if docstrNode is not None and isinstance(docstrNode, (Str, )):
                    return docstrNode
        return None

    @classmethod
    def resolveExpr(cls, n, s):
        return n.resolve(s)

    def resolve(self, s):
        pass

    def isCall(self):
        from Call import Call        
        return isinstance(self, (Call, ))

    def isModule(self):
        from Module import Module
        return isinstance(self, (Module, ))

    def isClassDef(self):
        return False

    def isFunctionDef(self):
        return False

    def isLambda(self):
        return False

    def isName(self):
        from Name import Name
        return isinstance(self, (Name, ))

    def isGlobal(self):
        from Global import Global
        return isinstance(self, (Global, ))

    def asCall(self):
        return self

    def asModule(self):
        return self

    def asClassDef(self):
        return self

    def asFunctionDef(self):
        return self

    def asLambda(self):
        return self

    def asName(self):
        return self

    def asGlobal(self):
        return self

    def addWarning(self, msg):
        from pysonarsq.java.Analyzer import Analyzer
        Analyzer.self.putProblem(self, msg)

    def addError(self, msg):
        from pysonarsq.java.Analyzer import Analyzer
        Analyzer.self.putProblem(self, msg)

    # 
    #      * Utility method to resolve every node in {@code nodes} and
    #      * return the union of their types.  If {@code nodes} is empty or
    #      * {@code null}, returns a new {@link org.yinwang.pysonar.types.UnknownType}.
    #      
    def resolveListAsUnion(self, nodes, s):
        from pysonarsq.java.Analyzer import Analyzer
        if nodes is None or len(nodes) == 0:
            return Analyzer.self.builtins.unknown
        result = Analyzer.self.builtins.unknown
        for node in nodes:
            nodeType = self.resolveExpr(node, s)
            result = UnionType.union(result, nodeType)
        return result

    # 
    #      * Resolves each element of a node list in the passed scope.
    #      * Node list may be empty or {@code null}.
    #      
    @classmethod
    def resolveList(cls, nodes, s):
        if nodes is not None:
            for n in nodes:
                cls.resolveExpr(n, s)

    @classmethod
    def resolveAndConstructList(cls, nodes, s):
        if nodes is None:
            return None
        else:
            typeList = []
            for n in nodes:
                typeList.append(cls.resolveExpr(n, s))
            return typeList

    def toDisplay(self):
        return ""

    def visit(self, visitor):
        pass

    def visitNode(self, n, v):
        if n is not None:
            n.visit(v)

    def visitNodeList(self, nodes, v):
        if nodes is not None:
            for n in nodes:
                if n is not None:
                    n.visit(v)

