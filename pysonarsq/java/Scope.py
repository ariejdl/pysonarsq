#!/usr/bin/env python

# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast import *

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

import java.util

from _ import _

from java.util import HashSet
from java.util import HashMap
from java.util import Map
from java.util import List
from java.util import Set

from Binding import Binding

#(from java.util import Map.Entry)

class _ScopeType(object):
    CLASS = u'CLASS'
    INSTANCE = u'INSTANCE'
    FUNCTION = u'FUNCTION'
    MODULE = u'MODULE'
    GLOBAL = u'GLOBAL'
    SCOPE = u'SCOPE'

class Scope(object):

    #@overloaded
    def __init__(self, parent=None, type_=None):
        #  stays null for most scopes (mem opt)
        #  all are non-null except global table
        #  link to the closest non-class scope, for lifting functions out
            # ....          
        
        if not hasattr(self, 'scopeType'):
            self.scopeType = None
        
        self.supers = List()
        self.globalNames = Set()
        self.type_ = None
        self.path = ""        
        self.parent = parent
        self.setScopeType(type_)
        self.forwarding = None
        self.table = Map()
    
        if isinstance(parent, Scope) and type_ is None:
            s = parent # case of creating a new scope from an existing one
            if s.table is not None:
                self.table = HashMap()
                self.table.update(s.table)
                self.parent = s.parent
                self.setScopeType(s.scopeType)
                self.forwarding = s.forwarding
                self.supers = s.supers
                self.globalNames = s.globalNames
            self.type_ = s.type_
            self.path = s.path        
        elif parent is not None:
            self.parent = parent
            self.setScopeType(type_)
            if type_ == self.ScopeType.CLASS:
                self.forwarding = (None if parent is None else parent.getForwarding())
            else:
                self.forwarding = self
                
    #  erase and overwrite this to s's contents
    def overwrite(self, s):
        self.table = s.table
        self.parent = s.parent
        self.setScopeType(s.scopeType)
        self.forwarding = s.forwarding
        self.supers = s.supers
        self.globalNames = s.globalNames
        self.type_ = s.type_
        self.path = s.path
        
    def copy(self):
        return Scope(self)

    #@overloaded
    def _merge(self, other):
        for e1 in self.getInternalTable().items():
            b1 = e1[1]
            b2 = other.getInternalTable().get(e1[0])
            #  both branch have the same name, need merge
            if b2 is not None and b1 != b2:
                b1 += b2
                
        for e2 in other.getInternalTable().items():
            
            b1 = self.getInternalTable().get(e2[0]);
            b2 = e2[1]
            #  both branch have the same name, need merge
            if b1 is None and b1 != b2:
                self.update(e2[0], b2)
                
        return self

    @classmethod
    def merge(cls, scope1, scope2=None):
        if scope2 is not None:
            return scope1._merge(scope2)
        else:
            ret = scope1.copy()
            ret.merge(scope2)
            return ret

    def setParent(self, parent):
        if parent is not None:
            self.parent = parent

    def getParent(self):
        return self.parent

    def getForwarding(self):
        if self.forwarding is not None:
            return self.forwarding
        else:
            return self

    def addSuper(self, sup):
        if self.supers is None:
            self.supers = ArrayList()
        self.supers.append(sup)

    def setScopeType(self, type_):
        if type_ is not None:
            self.scopeType = type_

    def getScopeType(self):
        return self.scopeType

    def addGlobalName(self, name):
        if self.globalNames is None:
            self.globalNames = HashSet()
        self.globalNames.add(name)

    def isGlobalName(self, name):
        if self.globalNames is not None:
            return name in self.globalNames
        elif self.parent is not None:
            return self.parent.isGlobalName(name)
        else:
            return False

    def remove(self, _id):
        if self.table is not None:
            if _id in self.table: del self.table[_id]

    #  create new binding and insert
    def insert(self, id, node, type_, kind):
        b = Binding(id, node, type_, kind)
        if type_.isModuleType():
            b.setQname(type_.asModuleType().getQname())
        else:
            b.setQname(self.extendPath(id))
        self.update(id, b)

    #  directly insert a given binding
    #@overloaded
    def update(self, id, bs):
        if hasattr(bs, '__len__'):
            self.getInternalTable()[id] = bs
        else:
            bs = [bs]
            self.getInternalTable()[id] = bs
            
        return bs

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def getType(self):
        return self.type_

    def setType(self, type_):
        self.type_ = type_

    # 
    #      * Look up a name in the current symbol table only. Don't recurse on the
    #      * parent table.
    #      
    def lookupLocal(self, name):
        if self.table is None:
            return None
        else:
            return self.table.get(name)

    # 
    #      * Look up a name (String) in the current symbol table.  If not found,
    #      * recurse on the parent table.
    #      
    def lookup(self, name):
        b = self.getModuleBindingIfGlobal(name)
        if b is not None:
            return b
        else:
            ent = self.lookupLocal(name)
            if ent is not None:
                return ent
            elif self.getParent() is not None:
                return self.getParent().lookup(name)
            else:
                return None

    # 
    #      * Look up a name in the module if it is declared as global, otherwise look
    #      * it up locally.
    #      
    def lookupScope(self, name):
        b = self.getModuleBindingIfGlobal(name)
        if b is not None:
            return b
        else:
            return self.lookupLocal(name)

    # 
    #      * Look up an attribute in the type hierarchy.  Don't look at parent link,
    #      * because the enclosing scope may not be a super class. The search is
    #      * "depth first, left to right" as in Python's (old) multiple inheritance
    #      * rule. The new MRO can be implemented, but will probably not introduce
    #      * much difference.
    #      
    looked = HashSet()

    #  circularity prevention
    def lookupAttr(self, attr):
        if self in self.looked:
            return None
        else:
            b = self.lookupLocal(attr);
            if b is not None:
                return b
            else:
                if self.supers is not None and len(self.supers):
                    self.looked.add(self)
                    for p in self.supers:
                        b = p.lookupAttr(attr)
                        if b is not None:
                            self.looked.remove(self)
                            return b
                    self.looked.remove(self)
                    return None
                else:
                    return None

    # 
    #      * Look for a binding named {@code name} and if found, return its type.
    #      
    def lookupType(self, name):
        bs = self.lookup(name)
        if bs is None:
            return None
        else:
            return self.makeUnion(bs)

    # 
    #      * Look for a attribute named {@code attr} and if found, return its type.
    #      
    def lookupAttrType(self, attr):
        bs = self.lookupAttr(attr)
        if bs is None:
            return None
        else:
            return self.makeUnion(bs)

    @classmethod
    def makeUnion(cls, bs):
        from pysonarsq.java.Analyzer import Analyzer

        t = Analyzer.self.builtins.unknown
        for b in bs:
            t = UnionType.union(t, b.getType())
            
        return t

    # 
    #      * Find a symbol table of a certain type in the enclosing scopes.
    #      
    def getSymtabOfType(self, type_):
        if self.scopeType == type_:
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.getSymtabOfType(type_)

    # 
    #      * Returns the global scope (i.e. the module scope for the current module).
    #      
    def getGlobalTable(self):
        result = self.getSymtabOfType(self.ScopeType.MODULE)
        if result is not None:
            return result
        else:
            _.die("Couldn't find global table. Shouldn't happen")
            return self

    # 
    #      * If {@code name} is declared as a global, return the module binding.
    #      
    def getModuleBindingIfGlobal(self, name):
        if self.isGlobalName(name):
            module_ = self.getGlobalTable();
            if module_ != self:
                return module_.lookupLocal(name)
        return None

    def putAll(self, other):
        self.getInternalTable().update(other.getInternalTable())

    def keySet(self):
        if self.table is not None:
            return self.table.items()
        else:
            return set()

    def values(self):
        if self.table is not None:
            ret = list()
            for bs in self.table.values():
                ret += bs
            return ret
        return Collections.emptySet()

    def entrySet(self):
        if self.table is not None:
            return self.table.items()
        return set()

    def isEmpty(self):
        return self.table is None or self.table.isEmpty()

    def extendPath(self, name):
        name = _.moduleName(name)
        if self.path == "":
            return name
        return self.path + "." + name

    def getInternalTable(self):
        if self.table is None:
            self.table = HashMap()
        return self.table

    def __str__(self):
        return "<Scope:" + str(self.getScopeType()) + ":" + str("{}" if self.table is None else self.table.items()) + ">"

Scope.ScopeType = _ScopeType
