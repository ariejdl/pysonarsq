#!/usr/bin/env python
""" generated source for module Withitem """
# package: org.yinwang.pysonar.ast
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable


from pysonarsq.java.Scope import Scope

from pysonarsq.java.types.Type import Type

from Node import Node
# 
#  * A name alias.  Used for the components of import and import-from statements.
#  
class Withitem(Node):
    """ generated source for class Withitem """

    def __init__(self, context_expr, optional_vars, start, end):
        """ generated source for method __init__ """
        super(Withitem, self).__init__(start, end)
        self.context_expr = context_expr
        self.optional_vars = optional_vars
        self.addChildren(context_expr, optional_vars)

    def __str__(self):
        """ generated source for method toString """
        return "<withitem:" + self.context_expr + " as " + self.optional_vars + ">"

    #  dummy, will never be called
    def resolve(self, s):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method resolve """
        return Analyzer.self.builtins.unknown

    def visit(self, v):
        """ generated source for method visit """
        if v.visit(self):
            self.visitNode(self.context_expr, v)
            self.visitNode(self.optional_vars, v)

