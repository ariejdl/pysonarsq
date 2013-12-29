#!/usr/bin/env python
""" generated source for module Analyzer """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull
from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast.Url import Url
from pysonarsq.java.ast.Call import Call

from pysonarsq.java.types.FunType import FunType
from pysonarsq.java.types.ModuleType import ModuleType
from pysonarsq.java.types.Type import Type

from java.io import File

import java.util

from java.util import ArrayList

from pysonarsq.java.Scope import Scope

from Ref import Ref

#(from java.util import Map.Entry)

from _ import _

from java.util import Set
from java.util import LinkedHashMap
from java.util import HashMap
from java.util import HashSet

from AstCache import AstCache
from Stats import Stats
from Builtins import Builtins
from FancyProgress import FancyProgress
from Diagnostic import Diagnostic

import logging
import os

def try_analyze(fileOrDir, analyzer=None):
    rootDir = _.parentFile(fileOrDir) if os.path.isfile(fileOrDir) else fileOrDir
    rootPath = _.unifyPath(rootDir)

    if analyzer is None:
        analyzer = Analyzer()

    analyzer.analyze(_.unifyPath(fileOrDir))
    analyzer.finish()
    analyzer.close()

    return analyzer


class Analyzer(object):
    #  global static instance of the analyzer itself
    #self = Analyzer()

    allBindings = ArrayList()
    references = LinkedHashMap()
    semanticErrors = HashMap()
    parseErrors = HashMap()
    cwd = None
    nCalled = 0
    multilineFunType = False
    path = ArrayList()
    uncalled = HashSet()
    callStack = HashSet()
    importStack = HashSet()
    astCache = AstCache()
    cacheDir = str()
    failedToParse = HashSet()
    stats = Stats()
    builtins = None # Builtins()
    logger = logging.getLogger(__name__)
    loadingProgress = None
    projectDir = str()
    
    # below doesn't work for some reason....
    """ 
    def init_vars(self):
        self.allBindings = ArrayList()
        self.references = LinkedHashMap()
        self.semanticErrors = HashMap()
        self.parseErrors = HashMap()
        self.cwd = None
        self.nCalled = 0
        self.multilineFunType = False
        self.path = ArrayList()
        self.uncalled = HashSet()
        self.callStack = HashSet()
        self.importStack = HashSet()
        self.astCache = AstCache()
        self.cacheDir = str()
        self.failedToParse = HashSet()
        self.stats = Stats()
        self.builtins = None # Builtins()
        self.logger = logging.getLogger(__name__)
        self.loadingProgress = None
        self.projectDir = str()   
        """        

    
    # singleton pattern
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Analyzer, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.moduleTable = Scope(None, Scope.ScopeType.GLOBAL)
        self.loadedFiles = ArrayList()
        self.globaltable = Scope(None, Scope.ScopeType.GLOBAL)            
            
        import time
        millis = int(round(time.time() * 1000))
        self.stats.putInt("startTime", millis)
        self.logger = logging.getLogger(__name__)
        
        if not hasattr(Analyzer, 'self'):
            setattr(Analyzer, 'self', self)
        
        self.builtins = Builtins()
        self.builtins.init()
        #self.addPythonPath()
        self.createCacheDir()
        self.getAstCache()
        
    #  main entry to the analyzer
    def analyze(self, path):
        self.projectDir = _.unifyPath(path)
        self.loadFileRecursive(self.projectDir)

    def setCWD(self, cd):
        if cd is not None:
            self.cwd = cd
        #if cd is not None:
        #    self.cwd = _.unifyPath(cd)

    def addPaths(self, p):
        for s in p:
            addPath(s)

    def addPath(self, p):
        self.path.add(_.unifyPath(p))

    def setPath(self, path):
        self.path = ArrayList(len(path))
        self.addPaths(path)

    def addPythonPath(self):
        path = System.getenv("PYTHONPATH")
        if path is not None:
            for p in segments:
                self.addPath(p)

    def getLoadPath(self):
        loadPath = ArrayList()
        if self.cwd is not None:
            loadPath.append(self.cwd)
        if self.projectDir is not None and os.path.isdir(self.projectDir):
            loadPath.append(self.projectDir)
        loadPath += self.path
        return loadPath

    def inStack(self, f):
        return f in self.callStack

    def pushStack(self, f):
        self.callStack.add(f)

    def popStack(self, f):
        self.callStack.remove(f)

    def inImportStack(self, f):
        return f in self.importStack

    def pushImportStack(self, f):
        self.importStack.add(f)

    def popImportStack(self, f):
        self.importStack.remove(f)

    def getAllBindings(self):
        return self.allBindings

    def getCachedModule(self, file_):
        t = self.moduleTable.lookupType(_.moduleQname(file_))
        if t is None:
            return None
        elif t.isUnionType():
            for tt in t.asUnionType().getTypes():
                if tt.isModuleType():
                    return tt
            return None
        elif t.isModuleType():
            return t
        else:
            return None

    def getDiagnosticsForFile(self, file_):
        errs = self.semanticErrors.get(file_)
        if errs is not None:
            return errs
        return ArrayList()

    #@overloaded
    def putRef(self, node, bs):
        if not hasattr(bs, '__len__'):
            bs = [bs]
            
        if not (isinstance(node, (Url, ))):
            ref = Ref(node);
            bindings = self.references.get(ref)
            if bindings is None:
                bindings = ArrayList()
                self.references[ref] = bindings
            for b in bs:
                if not b in bindings:
                    bindings.append(b)
                b.addRef(ref)

    def getReferences(self):
        """ generated source for method getReferences """
        return self.references
        
    def putProblem(self, *args):        
        if len(args) == 2:
            return self.putProblem0(*args)
        else:
            return self.putProblem1(*args)

    #@overloaded
    def putProblem0(self, loc, msg):
        """ generated source for method putProblem """
        file_ = loc.getFile()
        if file_ is not None:
            self.addFileErr(file_, loc.start, loc.end, msg)

    #  for situations without a Node
    #@putProblem.register(object, str, int, int, str)
    def putProblem1(self, file_, begin, end, msg):
        """ generated source for method putProblem_0 """
        if file_ is not None:
            self.addFileErr(file_, begin, end, msg)

    def addFileErr(self, file_, begin, end, msg):
        """ generated source for method addFileErr """
        d = Diagnostic(file_, Diagnostic.Category.ERROR, begin, end, msg)
        self.getFileErrs(file_, self.semanticErrors).append(d)

    def getParseErrs(self, file_):
        return self.getFileErrs(file_, self.parseErrors)

    def getFileErrs(self, file_, _map):
        msgs = _map.get(file_)
        if msgs is None:
            msgs = ArrayList()
            _map[file_] = msgs
        return msgs

    def loadFile(self, path):
        _.msg("loading: " + path);
        path = _.unifyPath(path)
        if not os.path.isfile(path):
            self.finer("\nfile not not found or cannot be read: " + path)
            return None
            
        module_ = self.getCachedModule(path)
        if module_ is not None:
            self.finer("\nusing cached module " + path + " [succeeded]")
            return module_
            
        #  detect circular import
        if Analyzer.self.inImportStack(path):
            return None
            
        #  set new CWD and save the old one on stack
        oldcwd = self.cwd
        
        self.setCWD( os.path.join(*path.split(os.sep)[:-1]) )
        Analyzer.self.pushImportStack(path)
        mod = self.parseAndResolve(path)

        #  restore old CWD
        self.setCWD(oldcwd)
        return mod

    def isInLoadPath(self, dir):
        for s in getLoadPath():
            if File(s) == dir:
                return True
        return False

    def parseAndResolve(self, file_):
        self.finer("Analyzing: " + file_)
        self.loadingProgress.tick()
        try:
            ast = self.getAstForFile(file_)
            if ast is None:
                self.failedToParse.add(file_)
                return None
            else:
                self.finer("resolving: " + file_)
                mod = ast.resolve(self.moduleTable)
                assert isinstance(mod, ModuleType)
                self.finer("[success]")
                self.loadedFiles.append(file_)
                return mod
        except MemoryError as e:
            if self.astCache is not None:
                self.astCache.clear()
            import gc
            gc.collect()
            return None

    def createCacheDir(self):
        """ generated source for method createCacheDir """
        self.cacheDir = _.makePathString(_.getSystemTempDir(), "pysonar2", "ast_cache")
        f = self.cacheDir
        _.msg("AST cache is at: " + self.cacheDir)
        if not os.path.exists(f):
            os.makedirs(f)
            if not os.path.exists(f):
                _.die("Failed to create tmp directory: " + self.cacheDir + ".Please check permissions")

    def getAstCache(self):
        """ generated source for method getAstCache """
        if self.astCache is None:
            self.astCache = AstCache.get()
        return self.astCache.INSTANCE

    # 
    #      * Returns the syntax tree for {@code file}. <p>
    #      
    def getAstForFile(self, file_):
        return self.getAstCache().getAST(file_)

    def getBuiltinModule(self, qname):
        return self.builtins.get(qname)

    def makeQname(self, names):
        if _.isEmpty(names):
            return ""
            
        ret = ""
        i = 0
        while i < len(names) - 1:
            ret += names[i].id + "."
            i += 1
        ret += names[len(names) - 1].id
        return ret

    # 
    #      * Find the path that contains modname. Used to find the starting point of locating a qname.
    #      *
    #      * @param headName first module name segment
    #      
    def locateModule(self, headName):
        loadPath = self.getLoadPath()
        
        for p in loadPath:
            startDir = os.sep.join([p, headName])
            initFile = _.joinPath(startDir, "__init__.py")
            
            if os.path.exists(initFile):
                return p
                
            startFile = startDir + ".py"
            if os.path.exists(startFile):
                return p
                
        return None

    def loadModule(self, name, scope):
        if _.isEmpty(name):
            return None
            
        from Binding import Binding
            
        qname = self.makeQname(name)
        mt = self.getBuiltinModule(qname)
        if mt is not None:
            scope.insert(name[0].id, Url(Builtins.LIBRARY_URL + mt.getTable().getPath() + ".html"), mt, Binding.Kind.SCOPE)
            return mt
            
        #  If there's more than one segment
        #  load the packages first
        prev = None
        startPath = self.locateModule(name[0].id)
        if startPath is None:
            return None

        path = startPath
        for i, n in enumerate(name):
            path = os.sep.join([path, name[i].id])
            initFile = _.joinPath(path, "__init__.py")
            
            if os.path.isfile(initFile):
                mod = self.loadFile(initFile)
                if mod is None:
                    return None
                if prev is not None:
                    prev.getTable().insert(name[i].id, name[i], mod, Binding.Kind.VARIABLE)
                else:
                    scope.insert(name[i].id, name[i], mod, Binding.Kind.VARIABLE)
                prev = mod
                
            elif i == len(name) - 1:
                startFile = path + ".py"
                if os.path.isfile(startFile):
                    mod = self.loadFile(startFile)
                    if mod is None:
                        return None
                    if prev is not None:
                        prev.getTable().insert(name[i].id, name[i], mod, Binding.Kind.VARIABLE)
                    else:
                        scope.insert(name[i].id, name[i], mod, Binding.Kind.VARIABLE)
                    prev = mod
                else:
                    return None
            
        return prev

    # 
    #      * Load all Python source files recursively if the given fullname is a
    #      * directory; otherwise just load a file.  Looks at file extension to
    #      * determine whether to load a given file.
    #      
    def loadFileRecursive(self, fullname):
        count = self.countFileRecursive(fullname)
        if self.loadingProgress is None:
            self.loadingProgress = FancyProgress(count, 50)
        if os.path.isdir(fullname):
            for root, dirs, files in os.walk(fullname):
                for f in files:
                    self.loadFileRecursive(root + os.sep + f)
                for d in dirs:
                    self.loadFileRecursive(root + os.sep + d)
        else:
            if fullname.endswith(".py"):
                self.loadFile(fullname)

    #  count number of .py files
    def countFileRecursive(self, fullname):
        sum = 0
        if os.path.isdir(fullname):
            for root, dirs, files in os.walk(fullname):
                for f in files:
                    sum += self.countFileRecursive(root + os.sep + f)
                for d in dirs:
                    sum += self.countFileRecursive(root + os.sep + d)
        else:
            if fullname.endswith(".py"):
                sum += 1
        return sum

    def finish(self):
        """ generated source for method finish """
        #         progress.end();
        _.msg("\nFinished loading files. " + str(self.nCalled) + " functions were called.")
        _.msg("Analyzing uncalled functions")
        self.applyUncalled()
        #  mark unused variables
        for b in self.allBindings:
            if not b.getType().isClassType() and not b.getType().isFuncType() and not b.getType().isModuleType() and _.isEmpty(b.getRefs()):
                Analyzer.self.putProblem(b.getNode(), "Unused variable: " + b.__class__.__name__)
        for ent in self.references.items():
            self.convertCallToNew(ent[0], ent[1])
        _.msg(self.getAnalysisSummary())

    def close(self):
        """ generated source for method close """
        self.astCache.close()

    def convertCallToNew(self, ref, bindings):
        """ generated source for method convertCallToNew """
        if ref.isRef():
            return
        if len(bindings) == 0:
            return
        nb = bindings[0]
        t = nb.getType()
        if t.isUnionType():
            t = t.asUnionType().firstUseful()
            if t is None:
                return
        if not t.isUnknownType() and not t.isFuncType():
            ref.markAsNew()

    def addUncalled(self, cl):
        """ generated source for method addUncalled """
        if not cl.func.called:
            self.uncalled.add(cl)

    def removeUncalled(self, f):
        if f in self.uncalled: self.uncalled.remove(f)

    def applyUncalled(self):
        """ generated source for method applyUncalled """
        progress = FancyProgress(len(self.uncalled), 50)
        while not _.isEmpty(self.uncalled):
            uncalledDup = list(self.uncalled)
            for cl in uncalledDup:
                progress.tick()
                Call.apply(cl, None, None, None, None, None)

    def getAnalysisSummary(self):
        sb = []
        sb.append("\n" + _.banner("analysis summary"))
        duration = _.formatTime(_.millis() - self.stats.getInt("startTime"))
        sb.append("\n- total time: " + duration)
        sb.append("\n- modules loaded: " + str(len(self.loadedFiles)))
        sb.append("\n- semantic problems: " + str(len(self.semanticErrors)))
        sb.append("\n- failed to parse: " + str(len(self.failedToParse)))
        #  calculate number of defs, refs, xrefs
        nDef = 0
        nXRef = 0
        for b in self.getAllBindings():
            nDef += 1
            nXRef += len(b.getRefs())
        sb.append("\n- number of definitions: " + str(nDef))
        sb.append("\n- number of cross references: " + str(nXRef))
        sb.append("\n- number of references: " + str(len(self.getReferences())))
        resolved = self.stats.getInt("resolved")
        unresolved = self.stats.getInt("unresolved")
        sb.append("\n- resolved names: " + str(resolved))
        sb.append("\n- unresolved names: " + str(unresolved))
        sb.append("\n- name resolve rate: " + _.percent(resolved, resolved + unresolved))
        sb.append("\n" + _.getGCStats())
        return ''.join(sb)

    def getLoadedFiles(self):
        files = ArrayList()
        for file_ in self.loadedFiles:
            if file_.endswith(".py"):
                files.append(file_)
        return files

    def registerBinding(self, b):
        self.allBindings.append(b)

    def log(self, level, msg):
        _.msg(msg)

    def severe(self, msg):
        self.log(Level.SEVERE, msg)

    def warn(self, msg):
        self.log(Level.WARNING, msg)

    def info(self, msg):
        self.log(Level.INFO, msg)

    def fine(self, msg):
        self.log(Level.FINE, msg)

    def finer(self, msg):
        self.log('*a log level*', msg)

    def __str__(self):
        return "<Analyzer:locs=" + len(self.references) + ":probs=" + len(self.semanticErrors) + ":files=" + len(self.loadedFiles) + ">"

