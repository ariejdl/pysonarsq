#!/usr/bin/env python
""" generated source for module Binder """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from pysonarsq.java.ast.Node import Node
from pysonarsq.java.ast.Name import Name
from pysonarsq.java.ast.Tuple import Tuple
from pysonarsq.java.ast.NList import NList
from pysonarsq.java.ast.Attribute import Attribute
from pysonarsq.java.ast.Subscript import Subscript

from pysonarsq.java.types.ListType import ListType

from pysonarsq.java.types.Type import Type

from pysonarsq.java.types.UnionType import UnionType

from java.util import List

# 
#  * Handles binding names to scopes, including destructuring assignment.
#  
class Binder(object):
    @classmethod
    #@overloaded
    def bind(cls, s, target, rvalue, kind=None):
        from Binding import Binding
        from pysonarsq.java.Analyzer import Analyzer
        from Scope import Scope
        
        if kind is None:
            kind = Binding.Kind()
            if s.getScopeType() == Scope.ScopeType.FUNCTION:
                kind = Binding.Kind.VARIABLE
            else:
                kind = Binding.Kind.SCOPE
        if isinstance(target, list):
            xs = target
            if rvalue.isTupleType():
                if len(xs) != len(vs):
                    reportUnpackMismatch(xs, len(vs))
                else:
                    while i < len(xs):
                        cls.bind(s, xs.get(i), vs.get(i), kind)
                        i += 1
            elif rvalue.isListType():
                cls.bind(s, xs, rvalue.asListType().toTupleType(len(xs)), kind)
            elif rvalue.isDictType():
                cls.bind(s, xs, rvalue.asDictType().toTupleType(len(xs)), kind)
            elif rvalue.isUnknownType():
                for x in xs:
                    cls.bind(s, x, Analyzer.self.builtins.unknown, kind)
            else:
                Analyzer.self.putProblem(xs.get(0).getFile(), xs.get(0).start, xs.get(len(xs) - 1).end, "unpacking non-iterable: " + rvalue)
            return
        

        if isinstance(target, (Name, )):
            name = target
            
            if (s.isGlobalName(name.id)):
                from Binding import Binding
                b = Binding(name.id, name, rvalue, kind);
                s.getGlobalTable().update(name.id, b)
                Analyzer.self.putRef(name, b)
            else:
                s.insert(name.id, name, rvalue, kind)                

        elif isinstance(target, (Tuple, )):
            cls.bind(s, (target).elts, rvalue, kind)
        elif isinstance(target, (NList, )):
            cls.bind(s, (target).elts, rvalue, kind)
        elif isinstance(target, (Attribute, )):
            (target).setAttr(s, rvalue)
        elif isinstance(target, (Subscript, )):
            sub = target;
            valueType = Node.resolveExpr(sub.value, s);
            
            Node.resolveExpr(sub.slice_, s)
            if isinstance(valueType, (ListType, )):
                
                t = valueType;
                t.setElementType(UnionType.union(t.getElementType(), rvalue))
        elif target is not None:
            Analyzer.self.putProblem(target, "invalid location for assignment")


    #  iterator
    @classmethod
    def bindIter(cls, s, target, iter, kind):
        iterType = Node.resolveExpr(iter, s)
        
        if iterType.isListType():
            cls.bind(s, target, iterType.asListType().getElementType(), kind)
        elif iterType.isTupleType():
            cls.bind(s, target, iterType.asTupleType().toListType().getElementType(), kind)
        else:
            ents = iterType.getTable().lookupAttr("__iter__");
            if ents is not None:
                for ent in ents:
                    if ent is None or not ent.getType().isFuncType():
                        if not iterType.isUnknownType():
                            Analyzer.self.putProblem(iter, "not an iterable type: " + iterType)
                        cls.bind(s, target, Analyzer.self.builtins.unknown, kind)
                    else:
                        cls.bind(s, target, ent.getType().asFuncType().getReturnType(), kind)
            else:
                from pysonarsq.java.Analyzer import Analyzer
                cls.bind(s, target, Analyzer.self.builtins.unknown, kind)

    @classmethod
    def reportUnpackMismatch(cls, xs, vsize):

        xsize = len(xs)
        beg = xs.get(0).start
        end = xs.get(len(xs) - 1).end
        diff = xsize - vsize
        msg = str()
        if diff > 0:
            msg = "ValueError: need more than " + vsize + " values to unpack"
        else:
            msg = "ValueError: too many values to unpack"
        Analyzer.self.putProblem(xs.get(0).getFile(), beg, end, msg)

