#!/usr/bin/env python
""" generated source for module DefaultNodeVisitor """
# package: org.yinwang.pysonar.ast
# 
#  * A visitor that by default visits every node in the tree.
#  * Subclasses can override specific node visiting methods
#  * and decide whether to visit the children.
#  
from NodeVisitor import NodeVisitor

class DefaultNodeVisitor(NodeVisitor):
    """ generated source for class DefaultNodeVisitor """
    def __init__(self):
        self.traverseIntoNodes = True

    # 
    #      * Once this is called, all {@code visit} methods will return {@code false}.
    #      * If the current node's children are being visited, all remaining top-level
    #      * children of the node will be visited (without visiting their children),
    #      * and then tree traversal halts. <p>
    #      * <p/>
    #      * If the traversal should be halted immediately without visiting any further
    #      * nodes, the visitor can throw a {@link StopIterationException}.
    #      
    def stopTraversal(self):
        """ generated source for method stopTraversal """
        self.traverseIntoNodes = False

    #@overloaded
    def visit(self, n):
        return self.traverseIntoNodes


