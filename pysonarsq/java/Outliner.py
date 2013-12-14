#!/usr/bin/env python
""" generated source for module Outliner """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.types.ModuleType import ModuleType

from pysonarsq.java.types.Type import Type

from java.util import ArrayList
from java.util import List
from java.util import Set
from java.util import TreeSet

import re

# 
#  * Generates a file outline from the index: a structure representing the
#  * variable and attribute definitions in a file.
#  
class Outliner(object):
    class Entry(object):

        #  binding kind of outline entry
        #@__init__.register(object, str, int, Binding.Kind)
        def __init__(self, qname, offset, kind):
            from Binding import Binding
            self.kind = Binding.Kind()
            self.qname = qname
            self.offset = offset
            self.kind = kind

        def isLeaf(self):
            raise Exception('abstract')                                    

        def asLeaf(self):
            return self

        def isBranch(self):
            raise Exception('abstract')                        

        def asBranch(self):
            return self

        def hasChildren(self):
            raise Exception('abstract')            

        def getChildren(self):
            raise Exception('abstract')

        def setChildren(self, children):
            raise Exception('abstract')            

        def getQname(self):
            return self.qname

        def setQname(self, qname):
            if qname is None:
                raise IllegalArgumentException("qname param cannot be null")
            self.qname = qname

        # 
        #          * Returns the file offset of the beginning of the identifier referenced
        #          * by this outline entry.
        #          
        def getOffset(self):
            return self.offset

        def setOffset(self, offset):
            self.offset = offset

        def getKind(self):
            return self.kind

        def setKind(self, kind):
            if kind is None:
                raise IllegalArgumentException("kind param cannot be null")
            self.kind = kind

        # 
        #          * Returns the simple (unqualified) name of the identifier.
        #          
        def getName(self):
            """ generated source for method getName """
            #parts = self.qname.split("[.&@%]")
            parts = re.split("[.&@%]", self.qname)
            return parts[-1]

        #@toString.register(object, StringBuilder, int)
        def __str__(self, sb=None, depth=None):
            if sb is None and depth is None:
                sb = []
                depth = 0
                
            i = 0
            while i < depth:
                sb.append("  ")
                i += 1
            sb.append(self.getKind())
            sb.append(" ")
            sb.append(self.__name__)
            sb.append("\n")
            if self.hasChildren():
                for e in getChildren():
                    e.toString(sb, depth + 1)

    # 
    #      * An outline entry with children.
    #      
    class Branch(Entry):

        def __init__(self, qname=None, start=None, kind=None):
            self.children = list()
            super(Outliner.Branch, self).__init__(qname, start, kind)

        def isLeaf(self):
            return False

        def isBranch(self):
            return True

        def hasChildren(self):
            return self.children is not None and not self.children.isEmpty()

        def getChildren(self):
            return self.children

        def setChildren(self, children):
            self.children = children

    # 
    #      * An entry with no children.
    #      
    class Leaf(Entry):
        def isLeaf(self):
            return True

        def isBranch(self):
            return False

        def __init__(self, qname=None, start=None, kind=None):
            super(Outliner.Leaf, self).__init__(qname, start, kind)

        def hasChildren(self):
            return False

        def getChildren(self):
            return ArrayList()

        def setChildren(self, children):
            raise UnsupportedOperationException("Leaf nodes cannot have children.")

    # 
    #      * Create an outline for a file in the index.
    #      *
    #      * @param scope the file scope
    #      * @param path  the file for which to build the outline
    #      * @return a list of entries constituting the file outline.
    #      *         Returns an empty list if the analyzer hasn't analyzed that path.
    #      
    #@overloaded
    def generate(self, idx, abspath):
        from Analyzer import Analyzer
        from Binding import Binding
        
        if isinstance(idx, Analyzer):
            mt = idx.loadFile(abspath)
            if mt is None:
                return ArrayList()
            scope, path = mt.getTable(), abspath
        else:
            scope, path = idx, abspath

        # alt impl.
        result = ArrayList()
        entries = TreeSet()
        for b in scope.values():
            if not b.isSynthetic() and not b.isBuiltin() and path == b.getFile():
                entries.add(b)
                
        entries = sorted(entries, lambda a,b: a.compareTo(b))
                
        for nb in entries:
            kids = None
            
            if nb.getKind() == Binding.Kind.CLASS:
                realType = nb.getType();
                if realType.isUnionType():
                    for t in realType.asUnionType().getTypes():
                        if t.isClassType():
                            realType = t
                            break
                kids = self.generate(realType.getTable(), path)
            
            kid = Outliner.Branch() if (kids is not None) else Outliner.Leaf();
            kid.setOffset(nb.getStart())
            kid.setQname(nb.getQname())
            kid.setKind(nb.getKind())
            if kids is not None:
                kid.setChildren(kids)
            result.append(kid)
        return result

