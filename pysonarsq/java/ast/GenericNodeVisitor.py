#!/usr/bin/env python
""" generated source for module GenericNodeVisitor """
# package: org.yinwang.pysonar.ast
# 
#  * A visitor that passes every visited node to a single function.
#  * Subclasses need only implement {@link #dispatch} to receive
#  * every node as a generic {@link Node}.
#  

from DefaultNodeVisitor import DefaultNodeVisitor
class GenericNodeVisitor(DefaultNodeVisitor):
    """ generated source for class GenericNodeVisitor """
    # 
    #      * Every visited node is passed to this method.  The semantics
    #      * for halting traversal are the same as for {@link DefaultNodeVisitor}.
    #      *
    #      * @return {@code true} to traverse this node's children
    #      
    def dispatch(self, n):
        """ generated source for method dispatch """
        return traverseIntoNodes

 

