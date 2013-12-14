#!/usr/bin/env python
""" generated source for module JSONDump """
# package: org.yinwang.pysonar
import com.fasterxml.jackson.core.JsonFactory

import com.fasterxml.jackson.core.JsonGenerator

import com.google.common.collect.Lists

from org.jetbrains.annotations import NotNull

from pysonarsq.java.ast import *

from pysonarsq.java.ast import *

from pysonarsq.java.ast import *

from pysonarsq.java.types.Type import Type

import java.io

import java.util

#(from java.util import Map.Entry)

#from java.util import logging.Level
#from java.util import logging.Logger

class JSONDump(object):
    """ generated source for class JSONDump """
    log = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME)
    seenDef = HashSet()
    seenRef = HashSet()
    seenDocs = HashSet()

    @classmethod
    def dirname(cls, path):
        """ generated source for method dirname """
        return File(path).getParent()

    @classmethod
    def newAnalyzer(cls, srcpath, inclpaths):
        """ generated source for method newAnalyzer """
        idx = Analyzer()
        for inclpath in inclpaths:
            idx.addPath(inclpath)
        idx.analyze(srcpath)
        idx.finish()
        if len(idx.semanticErrors) > 0:
            cls.log.info("Analyzer errors:")
            for entry in idx.semanticErrors.items():
                cls.log.info("  Key: " + k)
                for d in diagnostics:
                    cls.log.info("    " + d)
        return idx

    @classmethod
    def writeSymJson(cls, binding, json):
        """ generated source for method writeSymJson """
        if binding.getStart() < 0:
            return
        name = binding.__name__
        isExported = not (Binding.Kind.VARIABLE == binding.getKind() or Binding.Kind.PARAMETER == binding.getKind() or Binding.Kind.SCOPE == binding.getKind() or Binding.Kind.ATTRIBUTE == binding.getKind() or (0 == len(name) or name.charAt(0) == '_' or name.startswith("lambda%")))
        path = binding.getQname().replace('.', '/').replace("%20", ".")
        if not cls.seenDef.contains(path):
            cls.seenDef.add(path)
            json.writeStartObject()
            json.writeStringField("name", name)
            json.writeStringField("path", path)
            json.writeStringField("file", binding.getFileOrUrl())
            json.writeNumberField("identStart", binding.getStart())
            json.writeNumberField("identEnd", binding.getEnd())
            json.writeNumberField("defStart", binding.getBodyStart())
            json.writeNumberField("defEnd", binding.getBodyEnd())
            json.writeBooleanField("exported", isExported)
            json.writeStringField("kind", binding.getKind().__str__())
            if Binding.Kind.FUNCTION == binding.getKind() or Binding.Kind.METHOD == binding.getKind() or Binding.Kind.CONSTRUCTOR == binding.getKind():
                json.writeObjectFieldStart("funcData")
                if t.isUnionType():
                    t = t.asUnionType().firstUseful()
                if t is not None and t.isFuncType():
                    if func is not None:
                        args.append("(")
                        for n in func.getArgs():
                            if not first:
                                args.append(", ")
                            first = False
                            args.append(n.toDisplay())
                        if func.getVararg() is not None:
                            if not first:
                                args.append(", ")
                            first = False
                            args.append("*" + func.getVararg().toDisplay())
                        if func.getKwarg() is not None:
                            if not first:
                                args.append(", ")
                            first = False
                            args.append("**" + func.getKwarg().toDisplay())
                        args.append(")")
                        argExpr = args.__str__()
                json.writeNullField("params")
                json.writeStringField("signature", signature)
                json.writeEndObject()
            json.writeEndObject()

    @classmethod
    def writeRefJson(cls, ref, binding, json):
        """ generated source for method writeRefJson """
        if binding.getFile() is not None:
            if binding.getStart() >= 0 and ref.start() >= 0 and not binding.isBuiltin():
                json.writeStartObject()
                json.writeStringField("sym", path)
                json.writeStringField("file", ref.getFile())
                json.writeNumberField("start", ref.start())
                json.writeNumberField("end", ref.end())
                json.writeBooleanField("builtin", binding.isBuiltin())
                json.writeEndObject()

    @classmethod
    def writeDocJson(cls, binding, idx, json):
        """ generated source for method writeDocJson """
        path = binding.getQname().replace('.', '/').replace("%20", ".")
        if not cls.seenDocs.contains(path):
            cls.seenDocs.add(path)
            if doc is not None:
                json.writeStartObject()
                json.writeStringField("sym", path)
                json.writeStringField("file", binding.getFileOrUrl())
                json.writeStringField("body", doc.getStr())
                json.writeNumberField("start", doc.start)
                json.writeNumberField("end", doc.end)
                json.writeEndObject()

    @classmethod
    def shouldEmit(cls, pathToMaybeEmit, srcpath):
        """ generated source for method shouldEmit """
        return _.unifyPath(pathToMaybeEmit).startswith(_.unifyPath(srcpath))

    @classmethod
    def graph(cls, srcpath, inclpaths, symOut, refOut, docOut):
        """ generated source for method graph """
        parentDirs = Lists.newArrayList(inclpaths)
        parentDirs.add(cls.dirname(srcpath))
        
        def compare(a,b):
            return a - b
        
        parentDirs = sorted(parentDirs, compare)
        
        idx = cls.newAnalyzer(srcpath, inclpaths)
        idx.multilineFunType = True
        jsonFactory = JsonFactory()
        symJson = jsonFactory.createGenerator(symOut)
        refJson = jsonFactory.createGenerator(refOut)
        docJson = jsonFactory.createGenerator(docOut)
        allJson = [symJson, refJson, docJson]
        for json in allJson:
            json.writeStartArray()
        for b in idx.getAllBindings():
            if b.getFile() is not None:
                if cls.shouldEmit(b.getFile(), srcpath):
                    cls.writeSymJson(b, symJson)
                    cls.writeDocJson(b, idx, docJson)
            for ref in b.getRefs():
                if ref.getFile() is not None:
                    if not cls.seenRef.contains(key) and cls.shouldEmit(ref.getFile(), srcpath):
                        cls.writeRefJson(ref, b, refJson)
                        cls.seenRef.add(key)
        for json in allJson:
            json.writeEndArray()
            json.close()

    @classmethod
    def info(cls, msg):
        """ generated source for method info """
        print msg

    @classmethod
    def usage(cls):
        """ generated source for method usage """
        cls.info("Usage: java org.yinwang.pysonar.dump <source-path> <include-paths> <out-root> [verbose]")
        cls.info("  <source-path> is path to source unit (package directory or module file) that will be graphed")
        cls.info("  <include-paths> are colon-separated paths to included libs")
        cls.info("  <out-root> is the prefix of the output files.  There are 3 output files: <out-root>-doc, <out-root>-sym, <out-root>-ref")
        cls.info("  [verbose] if set, then verbose logging is used (optional)")

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if args.length > 4 or len(args):
            cls.usage()
            return
        cls.log.setLevel(Level.SEVERE)
        if len(args):
            cls.log.setLevel(Level.ALL)
            cls.log.info("LOGGING VERBOSE")
            cls.log.info("ARGS: " + Arrays.toString(args))
        srcpath = args[0]
        inclpaths = args[1].split(":")
        outroot = args[2]
        symFilename = outroot + "-sym"
        refFilename = outroot + "-ref"
        docFilename = outroot + "-doc"
        symOut = None
        refOut = None
        docOut = None
        try:
            docOut = BufferedOutputStream(FileOutputStream(docFilename))
            symOut = BufferedOutputStream(FileOutputStream(symFilename))
            refOut = BufferedOutputStream(FileOutputStream(refFilename))
            _.msg("graphing: " + srcpath)
            cls.graph(srcpath, inclpaths, symOut, refOut, docOut)
            docOut.flush()
            symOut.flush()
            refOut.flush()
        except FileNotFoundException as e:
            System.err.println("Could not find file: " + e)
            return
        finally:
            if docOut is not None:
                docOut.close()
            if symOut is not None:
                symOut.close()
            if refOut is not None:
                refOut.close()
        cls.log.info("SUCCESS")


if __name__ == '__main__':
    import sys
    JSONDump.main(sys.argv)

