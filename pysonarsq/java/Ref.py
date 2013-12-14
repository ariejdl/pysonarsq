#!/usr/bin/env python
""" generated source for module Ref """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast.Name import Name
from pysonarsq.java.ast.Attribute import Attribute

# 
#  * Encapsulates information about a binding reference.
#  
#class Ref(Comparable, object):
class Ref(object):    
    ATTRIBUTE = 0x1
    CALL = 0x2

    #  function/method call
    NEW = 0x4

    #  instantiation
    STRING = 0x8

    #@overloaded
    def __init__(self, path=None, offset=None, text=None):
        self.start_ = 0
        self.file_ = None
        self.name_ = None
        self.flags = 0
        
        if offset is not None and text is not None:
            self.file_ = path
            self.start_ = offset
            self.name_ = text
            return
        else:
            node = path
            
        # alt constructor
        self.file_ = node.getFile()
        self.start_ = node.start
        if isinstance(node, (Name, )):
            n = node
            self.name_ = n.id
            if n.isCall():
                self.markAsCall()
        elif isinstance(node, (Str, )):
            self.markAsString()
            self.name_ = (node).getStr()
        else:
            raise IllegalArgumentException("I don't know what " + node + " is.")
        parent = node.getParent()
        if (isinstance(parent, (Attribute, ))) and node == (parent).attr:
            self.markAsAttribute()
            
        if self.start_ is None:
            self.start_ = 0
            

    # 
    #      * Returns the file containing the reference.
    #      
    def getFile(self):
        return self.file_

    # 
    #      * Returns the text of the reference.
    #      
    def getName(self):
        return self.name_

    def start(self):
        return self.start_

    def end(self):
        return self.start_ + self.length()

    # 
    #      * Returns the length of the reference text.
    #      
    def length(self):
        return (2 + len(self.name_)) if self.isString() else len(self.name_)

    # 
    #      * Returns {@code true} if this reference was unquoted name.
    #      
    def isName(self):
        return not self.isString()

    # 
    #      * Returns {@code true} if this reference was an attribute
    #      * of some other node.
    #      
    def isAttribute(self):
        return (self.flags & self.ATTRIBUTE) != 0

    def markAsAttribute(self):
        self.flags |= self.ATTRIBUTE

    # 
    #      * Returns {@code true} if this reference was a quoted name.
    #      * If so, the {@link #start} and {@link #length} include the positions
    #      * of the opening and closing quotes, but {@link #isName} returns the
    #      * text within the quotes.
    #      
    def isString(self):
        return (self.flags & self.STRING) != 0

    def markAsString(self):
        self.flags |= self.STRING

    # 
    #      * Returns {@code true} if this reference is a function or method call.
    #      
    def isCall(self):
        return (self.flags & self.CALL) != 0

    # 
    #      * Returns {@code true} if this reference is a class instantiation.
    #      
    def markAsCall(self):
        self.flags |= self.CALL
        self.flags &= ~self.NEW

    def isNew(self):
        return (self.flags & self.NEW) != 0

    def markAsNew(self):
        self.flags |= self.NEW
        self.flags &= ~self.CALL

    def isRef(self):
        return not (self.isCall() or self.isNew())

    def __str__(self):
        return "<Ref:" + str(self.file_) + ":" + str(self.name_) + ":" + str(self.start_) + ">"
    
    #
    # in java equals and compareTo are used in hashmaps for keying
    #
    def __eq__(self, obj):
        if not (isinstance(obj, (Ref, ))):
            return False
        else:
            ref = obj;
            return (self.start_ == ref.start and (self.file_ is None and ref.file_ is None) or (self.file_ is not None and ref.file_ is not None and self.file_ == ref.file_))

    def compareTo(self, o):
        if isinstance(o, (Ref, )):
            return self.start_ - (o).start
        else:
            return -1
            
    def hashCode(self):
        return hash("" + (self.file_ if self.file_ is not None else '') + str(self.start_))
        
    def __hash__(self):
        return self.hashCode()
        
    def __cmp__(self, o):
        return self.compareTo(o)

