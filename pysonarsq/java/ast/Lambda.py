#!/usr/bin/env python

from org.jetbrains.annotations import NotNull


from pysonarsq.java.Binder import Binder
from pysonarsq.java.Binding import Binding
from pysonarsq.java.Scope import Scope
from pysonarsq.java.types.FunType import FunType
from pysonarsq.java.types.Type import Type

from java.util import List

from FunctionDef import FunctionDef

from Block import Block
from Name import Name

class Lambda(FunctionDef):
    def __init__(self, args, body, defaults, varargs, kwargs, start, end):
        super(Lambda, self).__init__(None, args, None, defaults, varargs, kwargs, start, end)
        self.body = body if isinstance(body, (Block, )) else body
        self.addChildren(self.body)

    def isLambda(self):
        return True

    @classmethod
    def genLambdaName(cls):
        if not hasattr(cls, 'lambdaCounter'): cls.lambdaCounter = 0
        cls.lambdaCounter = cls.lambdaCounter + 1
        return "lambda%" + str(cls.lambdaCounter)

    def getName(self):
        if self.name is not None:
            return self.name
        else:
            fn = self.genLambdaName();
            self.name = Name(fn, self.start, self.start + len('lambda'))
            self.addChildren(self.name)
            return self.name

    def resolve(self, outer):
        from pysonarsq.java.Analyzer import Analyzer

        self.defaultTypes = self.resolveAndConstructList(self.defaults, outer)
        cl = FunType(self, outer.getForwarding())
        cl.getTable().setParent(outer)
        cl.getTable().setPath(outer.extendPath(self.getName().id))
        Binder.bind(outer, self.getName(), cl, Binding.Kind.FUNCTION)
        cl.setDefaultTypes(self.resolveAndConstructList(self.defaults, outer))
        Analyzer.self.addUncalled(cl)
        
        return cl

    def __str__(self):
        return "<Lambda:" + str(self.start) + ":" + str(map(str, self.args)) + ":" + str(self.body) + ">"

    def visit(self, v):
        if v.visit(self):
            self.visitNodeList(self.args, v)
            self.visitNodeList(self.defaults, v)
            self.visitNode(self.vararg, v)
            self.visitNode(self.kwarg, v)
            self.visitNode(self.body, v)

