#!/usr/bin/env python
""" generated source for module Binding """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast import *
from pysonarsq.java.ast.Node import Node
from pysonarsq.java.ast.Url import Url
from pysonarsq.java.ast.FunctionDef import FunctionDef
from pysonarsq.java.ast.ClassDef import ClassDef
from pysonarsq.java.ast.Module import Module
from pysonarsq.java.ast.Name import Name


from pysonarsq.java.types.ModuleType import ModuleType

from pysonarsq.java.types.Type import Type

#from java.util import LinkedHashSet
from java.util import Set

from java.util import Set


#class Binding(Comparable, object):
class Binding(object):    
    """ generated source for class Binding """
    class Kind(object):
        """ generated source for enum Kind """
        ATTRIBUTE = u'ATTRIBUTE'
        CLASS = u'CLASS'
        CONSTRUCTOR = u'CONSTRUCTOR'
        FUNCTION = u'FUNCTION'
        METHOD = u'METHOD'
        MODULE = u'MODULE'
        PARAMETER = u'PARAMETER'
        SCOPE = u'SCOPE'
        VARIABLE = u'VARIABLE'

        #  attr accessed with "." on some other object
        #  class definition
        #  __init__ functions in classes
        #  plain function
        #  static or instance method
        #  file
        #  function param
        #  top-level variable ("scope" means we assume it can have attrs)
        #  local variable

    def __init__(self, id, node, type_, kind):
        from pysonarsq.java.Analyzer import Analyzer
        
        self.isStatic_ = False
        self.isSynthetic_ = False
        self.isReadonly_ = False
        self.isDeprecated_ = False
        self.isBuiltin_ = False
        self.name = str()
        self.qname = str()
        self.refs = Set()
        self.start = -1
        self.end = -1
        self.bodyStart = -1
        self.bodyEnd = -1
        self.fileOrUrl = str()        
        
        super(Binding, self).__init__()
        self.type_ = None
        self.name = id
        self.qname = type_.getTable().getPath()
        self.type_ = type_
        self.kind = kind
        self.node = node
        if isinstance(node, (Url, )):
            url = node
            if url.startswith("file://"):
                self.fileOrUrl = url.substring(len(length))
            else:
                self.fileOrUrl = url
        else:
            self.fileOrUrl = node.getFile()
            if isinstance(node, (Name, )):
                self.name = node.asName().id
        self.initLocationInfo(node)
        Analyzer.self.registerBinding(self)

    def initLocationInfo(self, node):
        """ generated source for method initLocationInfo """
        self.start = node.start
        self.end = node.end
        parent = node.getParent()
        if (isinstance(parent, (FunctionDef, )) and (parent).name == node) or (isinstance(parent, (ClassDef, )) and (parent).name == node):
            self.bodyStart = parent.start
            self.bodyEnd = parent.end
        elif isinstance(node, (Module, )):
            self.name = (node).name
            self.start = 0
            self.end = 0
            self.bodyStart = node.start
            self.bodyEnd = node.end
        else:
            self.bodyStart = node.start
            self.bodyEnd = node.end

    def getDocstring(self):
        parent = self.node.getParent()
        if (isinstance(parent, (FunctionDef, )) and (parent).name == self.node) or (isinstance(parent, (ClassDef, )) and (parent).name == self.node):
            return parent.getDocString()
        else:
            return self.node.getDocString()

    def getName(self):
        return self.name

    def setQname(self, qname):
        self.qname = qname

    def getQname(self):
        return self.qname

    def addRef(self, ref):
        self.getRefs().add(ref)

    def setType(self, type_):
        self.type_ = type_

    def getType(self):
        return self.type_

    def setKind(self, kind):
        self.kind = kind

    def getKind(self):
        return self.kind

    def markStatic(self):
        self.isStatic_ = True

    def isStatic(self):
        return self.isStatic_

    def markSynthetic(self):
        self.isSynthetic_ = True

    def isSynthetic(self):
        return self.isSynthetic_

    def markReadOnly(self):
        self.isReadonly_ = True

    def isBuiltin(self):
        return self.isBuiltin_

    def getRefs(self):
        if self.refs is None:
#            self.refs = LinkedHashSet(1)
            self.refs = Set(1)            
        return self.refs

    def getFirstFile(self):
        bt = self.getType()
        if isinstance(bt, (ModuleType, )):
            file_ = bt.asModuleType().getFile();
            return file_ if file_ is not None else "<built-in module>"
            
        file_ = self.getFile()
        if file_ is not None:
            return file_
        return "<built-in binding>"

    def getFile(self):
        return None if self.isURL() else self.fileOrUrl

    def getURL(self):
        return self.fileOrUrl if self.isURL() else None

    def getFileOrUrl(self):
        return self.fileOrUrl

    def isURL(self):
        return self.fileOrUrl is not None and self.fileOrUrl.startswith("http://")

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getLength(self):
        return self.end - self.start

    def getBodyStart(self):
        return self.bodyStart

    def getBodyEnd(self):
        return self.bodyEnd

    def getNode(self):
        return self.node

    # 
    #      * Bindings can be sorted by their location for outlining purposes.
    #      
    def compareTo(self, o):
        return (self.getStart() or 0) - (o.getStart() or 0)

    def __str__(self):
        sb = []
        
        sb.append("<Binding:")
        sb.append(":qname=")
        sb.append(self.qname)
        sb.append(":type=")
        sb.append(self.type_)
        sb.append(":kind=")
        sb.append(self.kind)
        sb.append(":node=")
        sb.append(self.node)
        sb.append(":refs=")
        if len(self.getRefs()) > 10:
            sb.append("[")
            sb.append(list(self.getRefs())[0])
            sb.append(", ...(")
            sb.append(len(self.getRefs()) - 1)
            sb.append(" more)]")
        else:
            sb.append([str(r) for r in self.refs])
        sb.append(">")
        
        sb = map(str, sb)
        return "".join(sb)

    def __eq__(self, obj):
        """ generated source for method equals """
        if not (isinstance(obj, (Binding, ))):
            return False
        else:
            b = obj
            return (self.start == b.start and self.end == b.end and ((self.fileOrUrl is None and b.fileOrUrl is None) or (self.fileOrUrl is not None and b.fileOrUrl is not None and self.fileOrUrl == b.fileOrUrl)))

    def hashCode(self):
        return hash("" + str(self.fileOrUrl) + (str(self.start) if self.start else ''))
        
    def __hash__(self):
        return self.hashCode()
        
    def __cmp__(self, o):
        return self.compareTo(o)

