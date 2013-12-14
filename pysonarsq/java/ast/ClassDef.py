#!/usr/bin/env python
""" generated source for module ClassDef """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

#import org.yinwang.pysonar

from pysonarsq.java.types.ClassType import ClassType
from pysonarsq.java.types.DictType import DictType
from pysonarsq.java.types.TupleType import TupleType
from pysonarsq.java.types.Type import Type

from java.util import ArrayList
from java.util import List

from Node import Node

class ClassDef(Node):
    """ generated source for class ClassDef """

    def __init__(self, name, bases, body, start, end):
        """ generated source for method __init__ """
        super(ClassDef, self).__init__(start, end)
        self.name = name
        self.bases = bases
        self.body = body
        self.addChildren(name, self.body)
        self.addChildren(bases)

    def isClassDef(self):
        """ generated source for method isClassDef """
        return True

    def getName(self):
        """ generated source for method getName """
        return self.name

    def bindsName(self):
        """ generated source for method bindsName """
        return True

    def resolve(self, s):
        from pysonarsq.java.Binder import Binder 
        from pysonarsq.java.Binding import Binding       
        from pysonarsq.java.Analyzer import Analyzer

        classType = ClassType(self.getName().id, s)
        baseTypes = ArrayList()
        for base in self.bases:
            baseType = self.resolveExpr(base, s);
            if baseType.isClassType():
                classType.addSuper(baseType)
            elif baseType.isUnionType():
                for b in baseType.asUnionType().getTypes():
                    classType.addSuper(b)
                    break
            else:
                Analyzer.self.putProblem(base, str(base) + " is not a class")
            baseTypes.append(baseType)
        #  XXX: Not sure if we should add "bases", "name" and "dict" here. They
        #  must be added _somewhere_ but I'm just not sure if it should be HERE.
        builtins = Analyzer.self.builtins
        self.addSpecialAttribute(classType.getTable(), "__bases__", TupleType(baseTypes))
        self.addSpecialAttribute(classType.getTable(), "__name__", builtins.BaseStr)
        self.addSpecialAttribute(classType.getTable(), "__dict__", DictType(builtins.BaseStr, Analyzer.self.builtins.unknown))
        self.addSpecialAttribute(classType.getTable(), "__module__", builtins.BaseStr)
        self.addSpecialAttribute(classType.getTable(), "__doc__", builtins.BaseStr)
        #  Bind ClassType to name here before resolving the body because the
        #  methods need this type as self.
        Binder.bind(s, self.name, classType, Binding.Kind.CLASS)
        self.resolveExpr(self.body, classType.getTable())
        return Analyzer.self.builtins.Cont

    def addSpecialAttribute(self, s, name, proptype):
        from pysonarsq.java.Binding import Binding
        from pysonarsq.java.Builtins import Builtins        
        """ generated source for method addSpecialAttribute """
        b = Binding(name, Builtins.newTutUrl("classes.html"), proptype, Binding.Kind.ATTRIBUTE)
        s.update(name, b)
        b.markSynthetic()
        b.markStatic()
        b.markReadOnly()

    def __str__(self):
        """ generated source for method toString """
        return "<ClassDef:" + str(self.name.id) + ":" + str(self.start) + ">"

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.name, v)
            self.visitNodeList(self.bases, v)
            self.visitNode(self.body, v)

