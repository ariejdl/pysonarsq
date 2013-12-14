#!/usr/bin/env python
""" generated source for module AstCache """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast import *

from java.util import HashMap
from java.util import Map

from java.io import File

import os
import pickle

from _ import _

#from java.util import logging.Level
#from java.util import logging.Logger

# 
#  * Provides a factory for python source ASTs.  Maintains configurable on-disk and
#  * in-memory caches to avoid re-parsing files during analysis.
#  

from PythonParser import PythonParser

class AstCache(object):
    """ generated source for class AstCache """
    cache = HashMap()
    parser = PythonParser()
    
    def __init__(self):
        """ generated source for method __init__ """

    @classmethod
    def get(cls):
        """ generated source for method get """
        if cls.INSTANCE is None:
            cls.INSTANCE = AstCache()
        cls.parser = PythonParser()
        return cls.INSTANCE

    # 
    #      * Clears the memory cache.
    #      
    def clear(self):
        """ generated source for method clear """
        self.cache.clear()

    # 
    #      * Removes all serialized ASTs from the on-disk cache.
    #      *
    #      * @return {@code true} if all cached AST files were removed
    #      
    def clearDiskCache(self):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method clearDiskCache """
        try:
            _.deleteDirectory(File(Analyzer.self.cacheDir))
            return True
        except Exception as x:
            AstCache.LOG.log(Level.SEVERE, "Failed to clear disk cache: " + x)
            return False

    def close(self):
        """ generated source for method close """
        self.parser.close()
        #         clearDiskCache();

    # 
    #      * Returns the syntax tree for {@code path}.  May find and/or create a
    #      * cached copy in the mem cache or the disk cache.
    #      *
    #      * @param path absolute path to a source file
    #      * @return the AST, or {@code null} if the parse failed for any reason
    #      
    def getAST(self, path):
        """ generated source for method getAST """
        #  Cache stores null value if the parse failed.
        if path in self.cache:
            return self.cache.get(path)
        #  Might be cached on disk but not in memory.
        mod = self.getSerializedModule(path)
        if mod is not None:
            AstCache.LOG.log(Level.FINE, "reusing " + path)
            self.cache[path] = mod
            return mod
        mod = None
        try:
            AstCache.LOG.log(1, "parsing " + path)
            mod = self.parser.parseFile(path)
        finally:
            self.cache[path] = mod
            #  may be null
        if mod is not None:
            self.serialize(mod)
        return mod

    # 
    #      * Each source file's AST is saved in an object file named for the MD5
    #      * checksum of the source file.  All that is needed is the MD5, but the
    #      * file's base name is included for ease of debugging.
    #      
    def getCachePath(self, md5, name=None): # stupid overridden crap
        from pysonarsq.java.Analyzer import Analyzer
        if name is None:
            md5 = _.getSHA1(md5)
            if isinstance(md5, file):
                name = md5.name
            else:
                name = md5
        
        """ generated source for method getCachePath_0 """
        return _.makePathString(Analyzer.self.cacheDir, name + md5 + ".ast")

    #  package-private for testing
    def serialize(self, ast):
        """ generated source for method serialize """
        filename = ast.getFile().split(os.sep)[-1]
        path = self.getCachePath(ast.getSHA1(), filename)
        
        with open(path, 'wb') as output:
            pickle.dump(ast, output)
            
        """
        oos = None
        fos = None
        try:
            fos = FileOutputStream(path)
            oos = ObjectOutputStream(fos)
            oos.writeObject(ast)
        except Exception as e:
            _.msg("Failed to serialize: " + path)
        finally:
            try:
                if oos is not None:
                    oos.close()
                elif fos is not None:
                    fos.close()
            except Exception as e:
                pass
        """                

    #  package-private for testing
    def getSerializedModule(self, sourcePath):
        """ generated source for method getSerializedModule """
        sourceFile = File(sourcePath)
        if not _.isReadableFile(sourcePath):
            return None
        cp = self.getCachePath(sourceFile)
        cpd = os.path.join(*cp.split(os.sep)[:-1])
        if not os.path.exists(cpd):
            os.makedirs(cpd)
            
        if not os.path.isfile(cp):
            return None
        return self.deserialize(sourceFile)

    #  package-private for testing
    def deserialize(self, sourcePath):
        """ generated source for method deserialize """
        cachePath = self.getCachePath(sourcePath)
        fis = None
        ois = None
        
        with open(sourcePath, 'rb') as _input:
            res = pickle.load(_input)
            return res
        
        """
        try:
            fis = FileInputStream(cachePath)
            ois = ObjectInputStream(fis)
            #  Files in different dirs may have the same base name and contents.
            mod.setFile(sourcePath)
            return mod
        except Exception as e:
            return None
        finally:
            try:
                if ois is not None:
                    ois.close()
                elif fis is not None:
                    fis.close()
            except Exception as e:
                pass
                """                
                
#class AstCache():
#    INSTANCE = _AstCache()      

AstCache.INSTANCE = AstCache()

import logging
AstCache.LOG = logging.getLogger(__name__)

