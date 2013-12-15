#!/usr/bin/env python
""" generated source for module PythonParser """
# package: org.yinwang.pysonar
#import com.google.gson.Gson
#import com.google.gson.GsonBuilder

from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

# java :)
from pysonarsq.java.ast.Alias import Alias
from pysonarsq.java.ast.Assert import Assert
from pysonarsq.java.ast.Assign import Assign
from pysonarsq.java.ast.Attribute import Attribute
from pysonarsq.java.ast.AugAssign import AugAssign
from pysonarsq.java.ast.BinOp import BinOp
from pysonarsq.java.ast.Block import Block
from pysonarsq.java.ast.BoolOp import BoolOp
from pysonarsq.java.ast.Break import Break
from pysonarsq.java.ast.Bytes import Bytes
from pysonarsq.java.ast.Call import Call
from pysonarsq.java.ast.ClassDef import ClassDef
from pysonarsq.java.ast.Compare import Compare
from pysonarsq.java.ast.Comprehension import Comprehension
from pysonarsq.java.ast.Continue import Continue
from pysonarsq.java.ast.DefaultNodeVisitor import DefaultNodeVisitor
from pysonarsq.java.ast.Delete import Delete
from pysonarsq.java.ast.Dict import Dict
from pysonarsq.java.ast.DictComp import DictComp
from pysonarsq.java.ast.Ellipsis import Ellipsis
from pysonarsq.java.ast.ExceptHandler import ExceptHandler
from pysonarsq.java.ast.Exec import Exec
from pysonarsq.java.ast.Expr import Expr
from pysonarsq.java.ast.ExtSlice import ExtSlice
from pysonarsq.java.ast.For import For
from pysonarsq.java.ast.FunctionDef import FunctionDef
from pysonarsq.java.ast.GeneratorExp import GeneratorExp
from pysonarsq.java.ast.GenericNodeVisitor import GenericNodeVisitor
from pysonarsq.java.ast.Global import Global
from pysonarsq.java.ast.If import If
from pysonarsq.java.ast.IfExp import IfExp
from pysonarsq.java.ast.Import import Import
from pysonarsq.java.ast.ImportFrom import ImportFrom
from pysonarsq.java.ast.Index import Index
from pysonarsq.java.ast.Keyword import Keyword
from pysonarsq.java.ast.Lambda import Lambda
from pysonarsq.java.ast.ListComp import ListComp
from pysonarsq.java.ast.Module import Module
from pysonarsq.java.ast.Name import Name
from pysonarsq.java.ast.NList import NList
from pysonarsq.java.ast.Node import Node
from pysonarsq.java.ast.NodeVisitor import NodeVisitor
from pysonarsq.java.ast.Num import Num
from pysonarsq.java.ast.Pass import Pass
from pysonarsq.java.ast.Print import Print
from pysonarsq.java.ast.Raise import Raise
from pysonarsq.java.ast.Repr import Repr
from pysonarsq.java.ast.Return import Return
from pysonarsq.java.ast.Sequence import Sequence
from pysonarsq.java.ast.Set import Set
from pysonarsq.java.ast.SetComp import SetComp
from pysonarsq.java.ast.Slice import Slice
from pysonarsq.java.ast.Str import Str
from pysonarsq.java.ast.Subscript import Subscript
from pysonarsq.java.ast.TryExcept import TryExcept
from pysonarsq.java.ast.TryFinally import TryFinally
from pysonarsq.java.ast.Tuple import Tuple
from pysonarsq.java.ast.UnaryOp import UnaryOp
from pysonarsq.java.ast.Url import Url
from pysonarsq.java.ast.While import While
from pysonarsq.java.ast.With import With
from pysonarsq.java.ast.Withitem import Withitem
from pysonarsq.java.ast.Yield import Yield
from pysonarsq.java.ast.YieldFrom import YieldFrom

from java.io import File

#from java.io import InputStream
#from java.io import OutputStreamWriter

from java.util import ArrayList

from java.util import List

from java.util import Map

import json

import os

from _ import _

class PythonParser(object):
    """ generated source for class PythonParser """
    python2Process = None
    python3Process = None
    gson = {}
    PYTHON2_EXE = "python"
    PYTHON3_EXE = "python3"
    exchangeFile = str()
    endMark = str()
    pyStub = str()
    TIMEOUT = 5000

    def __init__(self):
        tmpDir = _.getSystemTempDir()
        sid = _.newSessionId()
        self.exchangeFile = _.makePathString(tmpDir, "pysonar2", "json." + sid)
        self.endMark = _.makePathString(tmpDir, "pysonar2", "end." + sid)
        self.pyStub = _.makePathString(tmpDir, "pysonar2", "ast2json." + sid)
        # =) you ARE a python process =)
        #self.startPythonProcesses()
        if self.python2Process is not None:
            _.msg("Started: " + self.PYTHON2_EXE)
        if self.python3Process is not None:
            _.msg("Started: " + self.PYTHON3_EXE)

    def close(self):
        if os.path.exists(self.pyStub): os.remove(self.pyStub)
        if os.path.exists(self.exchangeFile): os.remove(self.exchangeFile)
        if os.path.exists(self.endMark): os.remove(self.endMark)

    def deserialize(self, text):
        return json.loads(text)

    def convertBlock(self, o):
        if o is None:
            return None
        else:
            return Block(self.convertList(o), 0, 0)

    def convertList(self, o):
        if o is None:
            return None
        else:
            in_ = o;
            out = []
            
            for m in in_:
                n = self.deJson(m)
                if n is not None:
                    out.append(n)
            return out

    def convertListKeyword(self, o):
        """ generated source for method self.convertListKeyword """
        if o is None:
            return None
        else:
            in_ = o
            out = []
            for m in in_:
                n = self.deJson(m);
                if n is not None:
                    out.append(n)
            return out

    def convertListExceptHandler(self, o):
        """ generated source for method self.convertListExceptHandler """
        if o is None:
            return None
        else:
            in_ = o
            out = []            
            for m in in_:
                n = self.deJson(m);
                if n is not None:
                    out.append(n)
            return out

    def convertListAlias(self, o):
        """ generated source for method self.convertListAlias """
        if o is None:
            return None
        else:
            in_ = o
            out = []            
            for m in in_:
                n = self.deJson(m);
                if n is not None:
                    out.append(n)
            return out

    def convertListComprehension(self, o):
        """ generated source for method self.convertListComprehension """
        if o is None:
            return None
        else:
            in_ = o
            out = []            
            for m in in_:
                n = self.deJson(m);
                if n is not None:
                    out.append(n)
            return out

    def segmentQname(self, qname, start, hasLoc):
        """ generated source for method segmentQname """
        result = ArrayList()
        i = 0
        while i < len(qname):
            name = "";
            
            while qname[i] in (' ', '\t', '\n'):
                i += 1
                
            nameStart = i;
            
            while i < len(qname) and (qname[i] not in (' ', '\t', '\n') or qname[i] == '*') and qname[i]!= '.':
                name += qname[i]
                i += 1
                
            nameStop = i;
            nstart = start + nameStart if hasLoc else -1;
            nstop = start + nameStop if hasLoc else -1;                
            result.append(Name(name, nstart, nstop))
            
            i += 1
        return result

    def deJson(self, o):
        """ generated source for method self.deJson """
        if not (isinstance(o, (Map, ))):
            return None
            
        _map = o
        type_ = str(_map.get("ast_type"))
        start = int(_map.get("node_start", 0))
        end = int(_map.get("node_end", 0))
        
        if type_ == "Module":
            b = self.convertBlock(_map.get("body"))
            m = Module(b, start, end)
            try:
                m.setFile(_.unifyPath(str(_map.get("filename"))))
            except Exception as e:
                pass
            return m
        if type_ == "alias":
            qname = _map.get("name")
            names = self.segmentQname(qname, start + len("import "), False);
            asname = None if _map.get("asname") is None else Name(_map.get("asname"))
            return Alias(names, asname, start, end)
        if type_ == "Assert":
            test = self.deJson(_map.get("test"))
            msg = self.deJson(_map.get("msg"))
            return Assert(test, msg, start, end)
        if type_ == "Assign":
            targets = self.convertList(_map.get("targets"))
            value = self.deJson(_map.get("value"));            
            return Assign(targets, value, start, end)
        if type_ == "Attribute":
            value = self.deJson(_map.get("value"));
            attr = self.deJson(_map.get("attr_name"));        
            assert isinstance(attr, Name)
            if attr is None:
                attr = Name(str(_map.get("attr")))
            return Attribute(value, attr, start, end)
        if type_ == "AugAssign":
            target = self.deJson(_map.get("target"));
            value = self.deJson(_map.get("value"));
            op = self.deJson(_map.get("op_node")); # h-a-c-k hack
            assert isinstance(op, Name)
            return AugAssign(target, value, op, start, end)
        if type_ == "BinOp":
            left = self.deJson(_map.get("left"));
            right = self.deJson(_map.get("right"));
            op = self.deJson(_map.get("op"));            
            return BinOp(left, right, op, start, end)
        if type_ == "BoolOp":
            values = self.convertList(_map.get("values"));
            op = self.deJson(_map.get("op_node")); 
            assert isinstance(op, Name)           
            return BoolOp(op, values, start, end)
        if type_ == "Break":
            return Break(start, end)
        if type_ == "Bytes":
            s = _map.get("s");            
            return Bytes(s, start, end)
        if type_ == "Call":
            func = self.deJson(_map.get("func"));
            args = self.convertList(_map.get("args"));
            keywords = self.convertListKeyword(_map.get("keywords"));
            kwargs = self.deJson(_map.get("kwarg"));
            starargs = self.deJson(_map.get("starargs"));
            return Call(func, args, keywords, kwargs, starargs, start, end)
        if type_ == "ClassDef":
            name = self.deJson(_map.get("name_node")) # hack
            assert isinstance(name, Name)
            bases = self.convertList(_map.get("bases"))
            body = self.convertBlock(_map.get("body"))
            return ClassDef(name, bases, body, start, end)
        if type_ == "Compare":
            name = self.deJson(_map.get("left"))
            ops = self.convertList(_map.get("ops"));
            comparators = self.convertList(_map.get("comparators"));            
            return Compare(name, ops, comparators, start, end)
        if type_ == "comprehension":
            target = self.deJson(_map.get("target"));
            _iter = self.deJson(_map.get("iter"));
            ifs = self.convertList(_map.get("ifs"));            
            return Comprehension(target, _iter, ifs, start, end)
        if type_ == "Continue":
            return Continue(start, end)
        if type_ == "Delete":
            targets = self.convertList(_map.get("targets"));            
            return Delete(targets, start, end)
        if type_ == "Dict":
            keys = self.convertList(_map.get("keys"));
            values = self.convertList(_map.get("values"));            
            return Dict(keys, values, start, end)
        if type_ == "DictComp":
            key = self.deJson(_map.get("key"));
            value = self.deJson(_map.get("value"));
            generators = self.convertListComprehension(_map.get("generators"));            
            return DictComp(key, value, generators, start, end)
        if type_ == "Ellipsis":
            return Ellipsis(start, end)
        if type_ == "ExceptHandler":
            name = self.deJson(_map.get("name"));
            exceptionType = self.deJson(_map.get("type"));
            body = self.convertBlock(_map.get("body"));            
            return ExceptHandler(name, exceptionType, body, start, end)
        if type_ == "Exec":
            body = self.deJson(_map.get("body"));
            _globals = self.deJson(_map.get("globals"));
            _locals = self.deJson(_map.get("locals"));            
            return Exec(body, _globals, _locals, start, end)
        if type_ == "Expr":
            value = self.deJson(_map.get("value"));            
            return Expr(value, start, end)
        if type_ == "For":
            target = self.deJson(_map.get("target"));
            _iter = self.deJson(_map.get("iter"));
            body = self.convertBlock(_map.get("body"));
            orelse = self.convertBlock(_map.get("orelse"));            
            return For(target, _iter, body, orelse, start, end)
        if type_ == "FunctionDef":
            name = self.deJson(_map.get("name_node"));
            assert isinstance(name, Name)
            args_map = _map.get("args");
            assert isinstance(args_map, dict)
            args = self.convertList(args_map.get("args"));
            defaults = self.convertList(args_map.get("defaults"));
            body = self.convertBlock(_map.get("body"));
            vararg = None if args_map.get("vararg") is None else Name(args_map.get("vararg"))
            kwarg = None if args_map.get("kwarg") is None else Name(args_map.get("kwarg"))
            return FunctionDef(name, args, body, defaults, vararg, kwarg, start, end)
        if type_ == "GeneratorExp":
            elt = self.deJson(_map.get("elt"));
            generators = self.convertListComprehension(_map.get("generators"));            
            return GeneratorExp(elt, generators, start, end)
        if type_ == "Global":
            names = list(_map.get("names"));
            nameNodes = list()
            for name in names:
                nameNodes.append(Name(name))
            return Global(nameNodes, start, end)
        if type_ == "If":
            test = self.deJson(_map.get("test"));
            body = self.convertBlock(_map.get("body"));
            orelse = self.convertBlock(_map.get("orelse"));            
            return If(test, body, orelse, start, end)
        if type_ == "IfExp":
            test = self.deJson(_map.get("test"));
            body = self.deJson(_map.get("body"));
            orelse = self.deJson(_map.get("orelse"));            
            return IfExp(test, body, orelse, start, end)
        if type_ == "Import":
            aliases = self.convertListAlias(_map.get("names"));            
            return Import(aliases, start, end)
        if type_ == "ImportFrom":
            module = _map.get("module");
            moduleSeg = None if module is None else self.segmentQname(module, start + len("from "), True)
            names = self.convertListAlias(_map.get("names"));
            level = int(_map.get("level"))
            return ImportFrom(moduleSeg, names, level, start, end)
        if type_ == "Index":
            value = self.deJson(_map.get("value"));            
            return Index(value, start, end)
        if type_ == "keyword":
            arg = _map.get("arg");
            value = self.deJson(_map.get("value"));            
            return Keyword(arg, value, start, end)
        if type_ == "Lambda":
            args_map = _map.get("args");
            assert isinstance(args_map, dict)
            args = self.convertList(args_map.get("args"));
            defaults = self.convertList(args_map.get("defaults"));
            body = self.deJson(_map.get("body"));
            vararg = None if args_map.get("vararg") is None else Name(args_map.get("vararg"))
            kwarg = None if args_map.get("kwarg") is None else Name(args_map.get("kwarg"))                      
            return Lambda(args, body, defaults, vararg, kwarg, start, end)
        if type_ == "List":
            elts = self.convertList(_map.get("elts"));            
            return NList(elts, start, end)
        if type_ == "ListComp":
            elt = self.deJson(_map.get("elt"));
            generators = self.convertListComprehension(_map.get("generators"));            
            return ListComp(elt, generators, start, end)
        if type_ == "Name":
            _id = _map.get("id");            
            return Name(_id, start, end)
        if type_ == "arg":
            _id = _map.get("arg");            
            return Name(_id, start, end)
        if type_ == "Num":
            n = _map.get("n");            
            return Num(n, start, end)
        if type_ == "SetComp":
            elt = self.deJson(_map.get("elt"));
            generators = self.convertListComprehension(_map.get("generators"));
            return SetComp(elt, generators, start, end)
        if type_ == "Pass":
            return Pass(start, end)
        if type_ == "Print":
            values = self.convertList(_map.get("values"));
            destination = self.deJson(_map.get("destination"));
            return Print(destination, values, start, end)
        if type_ == "Raise":
            exceptionType = self.deJson(_map.get("type"));
            inst = self.deJson(_map.get("inst"));
            tback = self.deJson(_map.get("tback"));            
            return Raise(exceptionType, inst, tback, start, end)
        if type_ == "Repr":
            value = self.deJson(_map.get("value"));
            return Repr(value, start, end)
        if type_ == "Return":
            value = self.deJson(_map.get("value"));
            return Return(value, start, end)
        if type_ == "Set":
            elts = self.convertList(_map.get("elts"));
            return Set(elts, start, end)
        if type_ == "SetComp":
            elt = self.deJson(_map.get("elt"));
            generators = self.convertListComprehension(_map.get("generators"));            
            return SetComp(elt, generators, start, end)
        if type_ == "Slice":
            lower = self.deJson(_map.get("lower"));
            step = self.deJson(_map.get("step"));
            upper = self.deJson(_map.get("upper"));            
            return Slice(lower, step, upper, start, end)
        if type_ == "ExtSlice":
            dims = self.convertList(_map.get("dims"));            
            return ExtSlice(dims, start, end)
        if type_ == "Str":
            s = _map.get("s");            
            return Str(s, start, end)
        if type_ == "Subscript":
            value = self.deJson(_map.get("value"));
            slice_ = self.deJson(_map.get("slice"));
            return Subscript(value, slice_, start, end)
        if type_ == "TryExcept":
            body = self.convertBlock(_map.get("body"));
            orelse = self.convertBlock(_map.get("orelse"));
            handlers = self.convertListExceptHandler(_map.get("handlers"));
            return TryExcept(handlers, body, orelse, start, end)
        if type_ == "TryFinally":
            body = self.convertBlock(_map.get("body"));
            finalbody = self.convertBlock(_map.get("finalbody"));
            return TryFinally(body, finalbody, start, end)
        if type_ == "Tuple":
            elts = self.convertList(_map.get("elts"));
            return Tuple(elts, start, end)
        if type_ == "UnaryOp":
            op = self.deJson(_map.get("op"));
            operand = self.deJson(_map.get("operand"));
            return UnaryOp(op, operand, start, end)
        if type_ == "While":
            test = self.deJson(_map.get("test"));
            body = self.convertBlock(_map.get("body"));
            orelse = self.convertBlock(_map.get("orelse"));
            return While(test, body, orelse, start, end)
        if type_ == "With":
            items = list()

            context_expr = self.deJson(_map.get("context_expr"));
            optional_vars = self.deJson(_map.get("optional_vars"));
            body = self.convertBlock(_map.get("body"));            
            
            if context_expr is not None:
                item = Withitem(context_expr, optional_vars, -1, -1);
                items.append(item)
            else:
                items_map = _map.get("items");
                assert isinstance(items_map, dict)
                for m in items_map:
                    context_expr = self.deJson(m.get("context_expr"))
                    optional_vars = self.deJson(m.get("optional_vars"))
                    item = Withitem(context_expr, optional_vars, -1, -1);
                    items.append(item)
            return With(items, body, start, end)
        if type_ == "Yield":
            value = self.deJson(_map.get("value"));
            return Yield(value, start, end)
        if type_ == "YieldFrom":
            value = self.deJson(_map.get("value"));
            return Yield(value, start, end)
        
        return None

    def prettyJson(self, json):
        obj = json.loads(json)
        return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))

    def startPython(self, pythonExe):
        try:
            fw.write(jsonizeStr)
            fw.close()
            builder.redirectErrorStream(True)
            builder.environment().remove("PYTHONPATH")
            return p
        except Exception as e:
            return None

    def parseFile(self, filename):
        from pysonarsq.java.Analyzer import Analyzer
        
        n2 = self.parseFileInner(filename, self.python2Process)
        if n2 is not None:
            return n2
        elif self.python3Process is not None:
            if n3 is None:
                Analyzer.self.failedToParse.append(filename)
                return None
            else:
                return n3
        else:
            Analyzer.self.failedToParse.add(filename)
            return None

    def parseFileInner(self, filename, pythonProcess):
        open(self.exchangeFile, 'a').close()
        open(self.endMark, 'a').close()
        
        s1 = _.escapeWindowsPath(filename);
        s2 = _.escapeWindowsPath(self.exchangeFile);
        s3 = _.escapeWindowsPath(self.endMark);        
        
        from pysonarsq.resources.ast2json import parse_dump
        parse_dump(s1, s2, s3)
        
        json = _.readFile(self.exchangeFile)
        
        # tidy up
        if os.path.exists(self.exchangeFile): os.remove(self.exchangeFile)
        if os.path.exists(self.endMark): os.remove(self.endMark)        
   
        _map = self.deserialize(json)
        return self.deJson(_map)

