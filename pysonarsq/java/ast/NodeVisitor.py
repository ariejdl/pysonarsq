#!/usr/bin/env python
""" generated source for module NodeVisitor """
# package: org.yinwang.pysonar.ast
# 
#  * Preorder-traversal node visitor interface.
#  

from abc import ABCMeta

class NodeVisitor(object):
    """ generated source for interface NodeVisitor """
    __metaclass__ = ABCMeta
    # 
    #      * Convenience exception for subclasses.  The caller that initiates
    #      * the visit should catch this exception if the subclass is expected
    #      * to throw it.
    #      
#    class StopIterationException(RuntimeException):
    class StopIterationException(Exception):        
        """ generated source for class StopIterationException """
        def __init__(self):
            """ generated source for method __init__ """
            super(NodeVisitor.StopIterationException, self).__init__()

    #@abstractmethod
    #@overloaded
    def visit(self, m):
        raise Exception('abstract')
        """ generated source for method visit """


