#!/usr/bin/env python
""" generated source for module Linker """
# package: org.yinwang.pysonar.demos
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from java.io import File

from java.util import HashMap
from java.util import HashSet

from pysonarsq.java._ import _
from pysonarsq.java.FancyProgress import FancyProgress

#(from java.util import Map.Entry)

from StyleRun import StyleRun

import re
import math

from pysonarsq.java.Binding import Binding
ATTRIBUTE = Binding.Kind.ATTRIBUTE
CLASS = Binding.Kind.CLASS
CONSTRUCTOR = Binding.Kind.CONSTRUCTOR
FUNCTION = Binding.Kind.FUNCTION
METHOD = Binding.Kind.METHOD
MODULE = Binding.Kind.MODULE
PARAMETER = Binding.Kind.PARAMETER
SCOPE = Binding.Kind.SCOPE
VARIABLE = Binding.Kind.VARIABLE

# 
#  * Collects per-file hyperlinks, as well as styles that require the
#  * symbol table to resolve properly.
#  
class Linker(object):
    """ generated source for class Linker """
    CONSTANT = re.compile("[A-Z_][A-Z0-9_]*")

    #  Map of file-path to semantic styles & links for that path.


    # 
    #      * Constructor.
    #      *
    #      * @param root   the root of the directory tree being indexed
    #      * @param outdir the html output directory
    #      
    def __init__(self, root=None, outdir=None):
        """ generated source for method __init__ """
        self.rootPath = root
        self.outDir = outdir

        self.fileStyles = HashMap()
        self.outDir = None #File()
        self.rootPath = str()
        self.seenDef = HashSet()
        self.seenRef = HashSet()        

    def findLinks(self, analyzer):
        """ generated source for method findLinks """
        _.msg("Adding xref links")
        progress = FancyProgress(len(analyzer.getAllBindings()), 50)
        for b in analyzer.getAllBindings():
            self.addSemanticStyles(b)
            self.processDef(b)
            progress.tick()
        #  highlight definitions
        _.msg("\nAdding ref links")
        progress = FancyProgress(len(analyzer.getReferences()), 50)
        for e in analyzer.getReferences().items():
            self.processRef(e[0], e[1])
            progress.tick()
        #         for (List<Diagnostic> ld: analyzer.semanticErrors.values()) {
        #             for (Diagnostic d: ld) {
        #                 processDiagnostic(d);
        #             }
        #         }
        #         for (List<Diagnostic> ld: analyzer.parseErrors.values()) {
        #             for (Diagnostic d: ld) {
        #                 processDiagnostic(d);
        #             }
        #         }

    def processDef(self, binding):
        """ generated source for method processDef """
        _hash = binding.hashCode()
        if binding.isURL() or binding.getStart() < 0 or _hash in self.seenDef:
            return
        self.seenDef.add(_hash)
        style = StyleRun(StyleRun.Type.ANCHOR, binding.getStart(), binding.getLength())
        style.message = binding.getType().__str__()
        style.url = binding.getQname()
        style.id = str(abs(binding.hashCode()))
        refs = binding.getRefs()
        style.highlight = list()
        for r in refs:
            style.highlight.append(str(abs(r.hashCode())))
        self.addFileStyle(binding.getFile(), style)

    def processRef(self, ref, bindings):
        """ generated source for method processRef """
        _hash = ref.hashCode()
        if not _hash in self.seenRef:
            self.seenRef.add(_hash)
            link = StyleRun(StyleRun.Type.LINK, ref.start(), ref.length());
            link.id = str(abs(_hash))
            
            typings = list()
            for b in bindings:
                typings.append(b.getType().__str__())
                
            if len(typings):
                if len(typings) > 1:
                    link.message = _.joinWithSep(typings, " | ", "{", "}")
                else:
                    link.message = typings[0]
            else:
                link.message = ''
                
            link.highlight = list()
            
            for b in bindings:
                link.highlight.append(str(abs(b.hashCode())))
            #  Currently jump to the first binding only. Should change to have a
            #  hover menu or something later.
            path = ref.getFile();
            for b in bindings:
                if link.url is None:
                    link.url = self.toURL(b, path)
                if link.url is not None:
                    self.addFileStyle(path, link)
                    break

    # 
    #      * Returns the styles (links and extra styles) generated for a given file.
    #      *
    #      * @param path an absolute source path
    #      * @return a possibly-empty list of styles for that path
    #      
    def getStyles(self, path):
        return self.stylesForFile(path)

    def stylesForFile(self, path):
        styles = self.fileStyles.get(path)
        if styles is None:
            styles = list()
            self.fileStyles[path] = styles
        return styles

    def addFileStyle(self, path, style):
        self.stylesForFile(path).append(style)

    # 
    #      * Add additional highlighting styles based on information not evident from
    #      * the AST.
    #      
    def addSemanticStyles(self, nb):
        isConst = self.CONSTANT.match(nb.__class__.__name__) is not None
        if nb.getKind()==SCOPE:
            if isConst:
                self.addSemanticStyle(nb, StyleRun.Type.CONSTANT)
        elif nb.getKind()==VARIABLE:
            self.addSemanticStyle(nb, StyleRun.Type.CONSTANT if isConst else StyleRun.Type.IDENTIFIER)
        elif nb.getKind()==PARAMETER:
            self.addSemanticStyle(nb, StyleRun.Type.PARAMETER)
        elif nb.getKind()==CLASS:
            self.addSemanticStyle(nb, StyleRun.Type.TYPE_NAME)

    def addSemanticStyle(self, binding, type_):
        path = binding.getFile()
        
        if binding.getStart() is None or binding.getEnd() is None:
            print('invalid binding: ' + str(binding))
            return
            
        if path is not None:
            self.addFileStyle(path, StyleRun(type_, binding.getStart(), binding.getLength()))

    def processDiagnostic(self, d):
        style = StyleRun(StyleRun.Type.WARNING, d.start, d.end - d.start)
        style.message = d.msg
        style.url = d.file_
        self.addFileStyle(d.file_, style)

    def toURL(self, binding, filename):
        if binding.isBuiltin():
            return binding.getURL()
        destPath = str()
        if binding.getType().isModuleType():
            destPath = binding.getType().asModuleType().getFile()
        else:
            destPath = binding.getFile()
        if destPath is None:
            return None
        anchor = "#" + binding.getQname()
        if binding.getFirstFile() == filename:
            return anchor
        if destPath.startswith(self.rootPath):
            if filename is not None:
                relpath = _.relPath(filename, destPath)
            else:
                relpath = destPath
            if relpath is not None:
                return relpath + ".html" + anchor
            else:
                return anchor
        else:
            return "file://" + destPath + anchor

