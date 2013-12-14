#!/usr/bin/env python
""" generated source for module Builtins """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from pysonarsq.java.ast import *
from pysonarsq.java.ast.Url import Url

from pysonarsq.java.types.ModuleType import ModuleType
from pysonarsq.java.types.ClassType import ClassType
from pysonarsq.java.types.InstanceType import InstanceType
from pysonarsq.java.types.FunType import FunType
from pysonarsq.java.types.TupleType import TupleType
from pysonarsq.java.types.ListType import ListType
from pysonarsq.java.types.DictType import DictType
from pysonarsq.java.types.UnionType import UnionType

from java.util import HashMap
from java.util import HashSet
from java.util import Map
from java.util import Set

from Binding import Binding
ATTRIBUTE = Binding.Kind.ATTRIBUTE
CLASS = Binding.Kind.CLASS
CONSTRUCTOR = Binding.Kind.CONSTRUCTOR
FUNCTION = Binding.Kind.FUNCTION
METHOD = Binding.Kind.METHOD
MODULE = Binding.Kind.MODULE
PARAMETER = Binding.Kind.PARAMETER
SCOPE = Binding.Kind.SCOPE
VARIABLE = Binding.Kind.VARIABLE

self_instance = None

class Builtins(object):

    LIBRARY_URL = "http://docs.python.org/library/"
    TUTORIAL_URL = "http://docs.python.org/tutorial/"
    REFERENCE_URL = "http://docs.python.org/reference/"
    DATAMODEL_URL = "http://docs.python.org/reference/datamodel#"

    @classmethod
    def newLibUrl(cls, path, extra=None):
        if extra:
            module_, name = path, extra
            return cls.newLibUrl(module_ + ".html#" + name)
        else:
            if not "#" in path and not path.endswith(".html"):
                path += ".html"
            return Url(cls.LIBRARY_URL + path)

    @classmethod
    def newRefUrl(cls, path):
        return Url(cls.REFERENCE_URL + path)

    @classmethod
    def newDataModelUrl(cls, path):
        return Url(cls.DATAMODEL_URL + path)

    @classmethod
    def newTutUrl(cls, path):
        return Url(cls.TUTORIAL_URL + path)


    def init_vars(self):
        """
        #  XXX:  need to model "types" module and reconcile with these types
        Builtin = None # Builtin()
        Object = None # ClassType()
        Type = None # ClassType()
        unknown = None # InstanceType()
        None_ = None # InstanceType()
        Cont = None # InstanceType()
        BaseNum = None # InstanceType()

        #  BaseNum models int, float and long
        BaseFloat = None # InstanceType()

        #  BaseNum models int, float and long
        BaseComplex = None # InstanceType()
        BaseBool = None # InstanceType()
        BaseStr = None # InstanceType()
        BaseList = None # ClassType()
        BaseArray = None # ClassType()
        BaseDict = None # ClassType()
        BaseTuple = None # ClassType()
        BaseModule = None # ClassType()
        BaseFile = None # ClassType()
        BaseFileInst = None # InstanceType()
        BaseException = None # ClassType()
        BaseStruct = None # ClassType()
        BaseFunction = None # ClassType()

        #  models functions, lambas and methods
        BaseClass = None # ClassType()

        #  models classes and instances
        Datetime_datetime = None # ClassType()
        Datetime_date = None # ClassType()
        Datetime_time = None # ClassType()
        Datetime_timedelta = None # ClassType()
        Datetime_tzinfo = None # ClassType()
        Time_struct_time = None # InstanceType()
        """
        
        self.builtin_exception_types = ["ArithmeticError", "AssertionError", "AttributeError", "BaseException",
                "Exception", "DeprecationWarning", "EOFError", "EnvironmentError", "FloatingPointError",
                "FutureWarning", "GeneratorExit", "IOError", "ImportError", "ImportWarning", "IndentationError",
                "IndexError", "KeyError", "KeyboardInterrupt", "LookupError", "MemoryError", "NameError",
                "NotImplemented", "NotImplementedError", "OSError", "OverflowError", "PendingDeprecationWarning",
                "ReferenceError", "RuntimeError", "RuntimeWarning", "StandardError", "StopIteration",
                "SyntaxError", "SyntaxWarning", "SystemError", "SystemExit", "TabError", "TypeError",
                "UnboundLocalError", "UnicodeDecodeError", "UnicodeEncodeError", "UnicodeError",
                "UnicodeTranslateError", "UnicodeWarning", "UserWarning", "ValueError", 
                "Warning", "ZeroDivisionError"]
                
        self.nativeTypes = HashSet()

    @classmethod
    def newClass(cls, name, table, superClass=None):
        obj = cls._get_self()
        
        if superClass is not None:
            moreSupers = []
            if hasattr(superClass, '__len__'):
                superClass, moreSupers = superClass
            t = ClassType(name, table, superClass)
            for c in moreSupers:
                t.addSuper(c)
            obj.nativeTypes.add(t)
            return t            
        else:
            t = ClassType(name, table, None)
            obj.nativeTypes.add(t)
            return t
    
    @classmethod
    def _get_self(self):
        """
        to resolve the ambiguity of the Builtins Class...
        """
        
        obj = None
        if isinstance(self, Builtins):
            obj = self
        else:
            global self_instance
            obj = self_instance 
        return obj              

    @classmethod
    def newModule(self, name):
        obj = self._get_self()
        
        from pysonarsq.java.Analyzer import Analyzer
        mt = ModuleType(name, None, Analyzer.self.globaltable)
        obj.nativeTypes.add(mt)
        return mt     

    @classmethod
    def getUnknown(self):
        obj = self._get_self()
        from pysonarsq.java.Analyzer import Analyzer

        t = Analyzer.self.builtins.unknown
        obj.nativeTypes.add(t)
        return t

    def newException(self, name, t):
        return Builtins.newClass(name, t, self.BaseException)

    @classmethod
    def newFunc(self, *args):
        obj = self._get_self()
        from pysonarsq.java.Analyzer import Analyzer
        
        type_ = None
        if args is not None and not args:
            type_ = FunType()
        elif args:
            type_ = args[0]
        
        if type_ is None:
            type_ = Analyzer.self.builtins.unknown
        t = FunType(Analyzer.self.builtins.unknown, type_)
        obj.nativeTypes.add(t)
        return t

    #@newList.register(object, self.Type)
    @classmethod
    def newList(self, type_=None):
        obj = self._get_self()
        if type_ is None:
            type_ = Builtins.getUnknown()

        t = ListType(type_)
        obj.nativeTypes.add(t)
        return t

    @classmethod
    def newDict(self, ktype, vtype):
        obj = self._get_self()
        t = DictType(ktype, vtype)
        obj.nativeTypes.add(t)
        return t

    @classmethod
    def newTuple(self, *types):
        obj = self._get_self()
        t = TupleType(*types)
        obj.nativeTypes.add(t)
        return t
        
    @classmethod
    def newUnion(self, *types):
        obj = self._get_self()
        t = UnionType(*types)
        obj.nativeTypes.add(t)
        return t

    @classmethod
    def list_(self, *names):
        return names

    class NativeModule(object):
        #name = str()
        #module_ = None # ModuleType()
        #from Scope import Scope
        #table = Scope()

        #  the module's symbol table
        def __init__(self, name):
            from Scope import Scope
            
            self.module_ = ModuleType()
            self.name = name
            self.table = Scope()
            Builtins.modules[name] = self

        # 
        #          * Lazily load the module.
        #          
        def getModule(self):
            if self.module_ is None:
                self.createModuleType()
                self.initBindings()
            return self.module_

        def initBindings(self):
            pass

        def createModuleType(self):
            from pysonarsq.java.Analyzer import Analyzer
            
            if self.module_ is None:
                self.module_ = Builtins.newModule(self.name)
                self.table = self.module_.getTable()
                Analyzer.self.moduleTable.insert(self.name, self.liburl(), self.module_, MODULE)

        def update(self, name, url, type_, kind):
            self.table.insert(name, url, type_, kind)

        def addClass(self, name, url, type_):
            self.table.insert(name, url, type_, CLASS)

        def addMethod(self, name, url, type_):
            self.table.insert(name, url, type_, METHOD)

        def addFunction(self, name, url, type_):
            self.table.insert(name, url, Builtins.newFunc(type_), FUNCTION)

        #  don't use this unless you're sure it's OK to share the type object
        def addFunctions_beCareful(self, type_, *names):
            for name in names:
                self.addFunction(self.name, liburl(), type_)

        def addNoneFuncs(self, *names):
            self.addFunctions_beCareful(self.None_, names)

        def addNumFuncs(self, *names):
            self.addFunctions_beCareful(self.BaseNum, names)

        def addStrFuncs(self, *names):
            self.addFunctions_beCareful(self.BaseStr, names)

        def addUnknownFuncs(self, *names):
            for name in names:
                self.addFunction(self.name, liburl(), Builtins.getUnknown())

        def addAttr(self, name, url, type_):
            self.table.insert(name, url, type_, ATTRIBUTE)

        #  don't use this unless you're sure it's OK to share the type object
        def addAttributes_beCareful(self, type_, *names):
            for name in names:
                self.addAttr(self.name, self.liburl(), type_)

        def addNumAttrs(self, *names):
            self.addAttributes_beCareful(Builtins.BaseNum, names)

        def addStrAttrs(self, *names):
            self.addAttributes_beCareful(Builtins.BaseStr, names)

        def addUnknownAttrs(self, *names):
            """ generated source for method addUnknownAttrs """
            for name in names:
                self.addAttr(self.name, self.liburl(), Builtins.getUnknown())

        #@liburl.register(object, str)
        def liburl(self, anchor=None):
            return Builtins.newLibUrl(self.name, anchor)

        def __str__(self):
            """ generated source for method toString """
            return "<Non-loaded builtin module '" + self.name + "'>" if self.module_ is None else "<NativeModule:" + self.module_ + ">"

    # 
    #      * The set of top-level native modules.
    #      
    modules = HashMap()

    def __init__(self):
        global self_instance
        self_instance = self
        self.init_vars()
        self.buildTypes()

    @classmethod
    def buildTypes(self):
        """ generated source for method buildTypes """
        self.BuiltinsModule(self)
        bt = self.Builtin.getTable()
        self.Object = Builtins.newClass("object", bt)
        self.unknown = InstanceType(Builtins.newClass("?", bt))
        self.None_ = InstanceType(Builtins.newClass("None", bt))
        self.Cont = InstanceType(Builtins.newClass("None", bt))
        #  continuation (to express non-return)
        self.Type = Builtins.newClass("type", bt, self.Object)
        self.BaseTuple = Builtins.newClass("tuple", bt, self.Object)
        self.BaseList = Builtins.newClass("list", bt, self.Object)
        self.BaseArray = Builtins.newClass("array", bt)
        self.BaseDict = Builtins.newClass("dict", bt, self.Object)
        numClass = Builtins.newClass("int", bt, self.Object)
        self.BaseNum = InstanceType(numClass)
        self.BaseFloat = InstanceType(Builtins.newClass("float", bt, self.Object))
        self.BaseComplex = InstanceType(Builtins.newClass("complex", bt, self.Object))
        self.BaseBool = InstanceType(Builtins.newClass("bool", bt, numClass))
        self.BaseStr = InstanceType(Builtins.newClass("str", bt, self.Object))
        self.BaseModule = Builtins.newClass("module", bt)
        self.BaseFile = Builtins.newClass("file", bt, self.Object)
        self.BaseFileInst = InstanceType(self.BaseFile)
        self.BaseFunction = Builtins.newClass("function", bt, self.Object)
        self.BaseClass = Builtins.newClass("classobj", bt, self.Object)


    def init(self):
        """ generated source for method init """
        self.buildObjectType()
        self.buildTupleType()
        self.buildArrayType()
        self.buildListType()
        self.buildDictType()
        self.buildNumTypes()
        self.buildStrType()
        self.buildModuleType()
        self.buildFileType()
        self.buildFunctionType()
        self.buildClassType()
        
        self.modules.get("__builtin__").initBindings()
        #  eagerly load these bindings
        Builtins.ArrayModule()
        Builtins.AudioopModule()
        Builtins.BinasciiModule()
        Builtins.Bz2Module()
        Builtins.CPickleModule()
        Builtins.CStringIOModule()
        Builtins.CMathModule()
        Builtins.CollectionsModule()
        Builtins.CryptModule()
        Builtins.CTypesModule()
        Builtins.DatetimeModule()
        Builtins.DbmModule()
        Builtins.ErrnoModule()
        Builtins.ExceptionsModule()
        Builtins.FcntlModule()
        Builtins.FpectlModule()
        Builtins.GcModule()
        Builtins.GdbmModule()
        Builtins.GrpModule()
        Builtins.ImpModule()
        Builtins.ItertoolsModule()
        Builtins.MarshalModule()
        Builtins.MathModule()
        Builtins.Md5Module()
        Builtins.MmapModule()
        Builtins.NisModule()
        Builtins.OperatorModule()
        Builtins.OsModule()
        Builtins.ParserModule()
        Builtins.PosixModule()
        Builtins.PwdModule()
        Builtins.PyexpatModule()
        Builtins.ReadlineModule()
        Builtins.ResourceModule()
        Builtins.SelectModule()
        Builtins.SignalModule()
        Builtins.ShaModule()
        Builtins.SpwdModule()
        Builtins.StropModule()
        Builtins.StructModule()
        Builtins.SysModule()
        Builtins.SyslogModule()
        Builtins.TermiosModule()
        Builtins.ThreadModule()
        Builtins.TimeModule()
        Builtins.UnicodedataModule()
        Builtins.ZipimportModule()
        Builtins.ZlibModule()

    # 
    #      * Loads (if necessary) and returns the specified built-in module.
    #      
    def get(self, name):
        """ generated source for method get """
        if not "." in name:
            #  unqualified
            return self.getModule(name)
        mods = name.split("\\.")
        type_ = self.getModule(mods[0])
        if type_ is None:
            return None
        i = 1
        while len(mods):
            type_ = type_.getTable().lookupType(mods[i])
            if not (isinstance(type_, (ModuleType, ))):
                return None
            i += 1
        return type_

    def getModule(self, name):
        """ generated source for method getModule """
        wrap = self.modules.get(name)
        return None if wrap is None else wrap.getModule()

    def isNative(self, type_):
        """ generated source for method isNative """
        return type_ in self.nativeTypes

    def buildObjectType(self):
        """ generated source for method buildObjectType """
        obj_methods = ["__delattr__", "__format__", "__getattribute__", "__hash__", "__init__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__sizeof__", "__str__", "__subclasshook__"]
        for m in obj_methods:
            self.Object.getTable().insert(m, Builtins.newLibUrl("stdtypes"), Builtins.newFunc(), METHOD)
        self.Object.getTable().insert("__doc__", Builtins.newLibUrl("stdtypes"), self.BaseStr, CLASS)
        self.Object.getTable().insert("__class__", Builtins.newLibUrl("stdtypes"), Builtins.getUnknown(), CLASS)

    def buildTupleType(self):
        """ generated source for method buildTupleType """
        bt = self.BaseTuple.getTable()
        tuple_methods = ["__add__", "__contains__", "__eq__", "__ge__", "__getnewargs__", "__gt__", "__iter__", "__le__", "__len__", "__lt__", "__mul__", "__ne__", "__new__", "__rmul__", "count", "index"]
        for m in tuple_methods:
            bt.insert(m, Builtins.newLibUrl("stdtypes"), Builtins.newFunc(), METHOD)
        bt.insert("__getslice__", self.newDataModelUrl("object.__getslice__"), Builtins.newFunc(), METHOD)
        bt.insert("__getitem__", self.newDataModelUrl("object.__getitem__"), Builtins.newFunc(), METHOD)
        bt.insert("__iter__", self.newDataModelUrl("object.__iter__"), Builtins.newFunc(), METHOD)

    def buildArrayType(self):
        """ generated source for method buildArrayType """
        array_methods_none = ["append", "buffer_info", "byteswap", "extend", "fromfile", "fromlist", "fromstring", "fromunicode", "index", "insert", "pop", "read", "remove", "reverse", "tofile", "tolist", "typecode", "write"]
        for m in array_methods_none:
            self.BaseArray.getTable().insert(m, Builtins.newLibUrl("array"), Builtins.newFunc(Builtins.None_), METHOD)
        array_methods_num = ["count", "itemsize"]
        for m in array_methods_num:
            self.BaseArray.getTable().insert(m, Builtins.newLibUrl("array"), Builtins.newFunc(Builtins.BaseNum), METHOD)
        array_methods_str = ["tostring", "tounicode"]
        for m in array_methods_str:
            self.BaseArray.getTable().insert(m, Builtins.newLibUrl("array"), Builtins.newFunc(Builtins.BaseStr), METHOD)

    def buildListType(self):
        """ generated source for method buildListType """
        self.BaseList.getTable().insert("__getslice__", self.newDataModelUrl("object.__getslice__"), Builtins.newFunc(self.BaseList), METHOD)
        self.BaseList.getTable().insert("__getitem__", self.newDataModelUrl("object.__getitem__"), Builtins.newFunc(self.BaseList), METHOD)
        self.BaseList.getTable().insert("__iter__", self.newDataModelUrl("object.__iter__"), Builtins.newFunc(self.BaseList), METHOD)
        list_methods_none = ["append", "extend", "index", "insert", "pop", "remove", "reverse", "sort"]
        for m in list_methods_none:
            self.BaseList.getTable().insert(m, Builtins.newLibUrl("stdtypes"), Builtins.newFunc(Builtins.None_), METHOD)
        list_methods_num = ["count"]
        for m in list_methods_num:
            self.BaseList.getTable().insert(m, Builtins.newLibUrl("stdtypes"), Builtins.newFunc(Builtins.BaseNum), METHOD)

    def numUrl(self):
        """ generated source for method numUrl """
        return Builtins.newLibUrl("stdtypes", "typesnumeric")

    def buildNumTypes(self):
        """ generated source for method buildNumTypes """
        bft = self.BaseFloat.getTable()
        float_methods_num = ["__abs__", "__add__", "__coerce__", "__div__", "__divmod__", "__eq__", "__float__", "__floordiv__", "__format__", "__ge__", "__getformat__", "__gt__", "__int__", "__le__", "__long__", "__lt__", "__mod__", "__mul__", "__ne__", "__neg__", "__new__", "__nonzero__", "__pos__", "__pow__", "__radd__", "__rdiv__", "__rdivmod__", "__rfloordiv__", "__rmod__", "__rmul__", "__rpow__", "__rsub__", "__rtruediv__", "__setformat__", "__sub__", "__truediv__", "__trunc__", "as_integer_ratio", "fromhex", "is_integer"]
        for m in float_methods_num:
            bft.insert(m, self.numUrl(), Builtins.newFunc(self.BaseFloat), METHOD)
        bnt = self.BaseNum.getTable()
        num_methods_num = ["__abs__", "__add__", "__and__", "__class__", "__cmp__", "__coerce__", "__delattr__", "__div__", "__divmod__", "__doc__", "__float__", "__floordiv__", "__getattribute__", "__getnewargs__", "__hash__", "__hex__", "__index__", "__init__", "__int__", "__invert__", "__long__", "__lshift__", "__mod__", "__mul__", "__neg__", "__new__", "__nonzero__", "__oct__", "__or__", "__pos__", "__pow__", "__radd__", "__rand__", "__rdiv__", "__rdivmod__", "__reduce__", "__reduce_ex__", "__repr__", "__rfloordiv__", "__rlshift__", "__rmod__", "__rmul__", "__ror__", "__rpow__", "__rrshift__", "__rshift__", "__rsub__", "__rtruediv__", "__rxor__", "__setattr__", "__str__", "__sub__", "__truediv__", "__xor__"]
        for m in num_methods_num:
            bnt.insert(m, self.numUrl(), Builtins.newFunc(self.BaseNum), METHOD)
        bnt.insert("__getnewargs__", self.numUrl(), Builtins.newFunc(Builtins.newTuple(self.BaseNum)), METHOD)
        bnt.insert("hex", self.numUrl(), Builtins.newFunc(self.BaseStr), METHOD)
        bnt.insert("conjugate", self.numUrl(), Builtins.newFunc(self.BaseComplex), METHOD)
        bct = self.BaseComplex.getTable()
        complex_methods = ["__abs__", "__add__", "__div__", "__divmod__", "__float__", "__floordiv__", "__format__", "__getformat__", "__int__", "__long__", "__mod__", "__mul__", "__neg__", "__new__", "__pos__", "__pow__", "__radd__", "__rdiv__", "__rdivmod__", "__rfloordiv__", "__rmod__", "__rmul__", "__rpow__", "__rsub__", "__rtruediv__", "__sub__", "__truediv__", "conjugate"]
        for c in complex_methods:
            bct.insert(c, self.numUrl(), Builtins.newFunc(self.BaseComplex), METHOD)
        complex_methods_num = ["__eq__", "__ge__", "__gt__", "__le__", "__lt__", "__ne__", "__nonzero__", "__coerce__"]
        for cn in complex_methods_num:
            bct.insert(cn, self.numUrl(), Builtins.newFunc(self.BaseNum), METHOD)
        bct.insert("__getnewargs__", self.numUrl(), Builtins.newFunc(Builtins.newTuple(self.BaseComplex)), METHOD)
        bct.insert("imag", self.numUrl(), self.BaseNum, ATTRIBUTE)
        bct.insert("real", self.numUrl(), self.BaseNum, ATTRIBUTE)

    def buildStrType(self):
        """ generated source for method buildStrType """
        self.BaseStr.getTable().insert("__getslice__", self.newDataModelUrl("object.__getslice__"), Builtins.newFunc(self.BaseStr), METHOD)
        self.BaseStr.getTable().insert("__getitem__", self.newDataModelUrl("object.__getitem__"), Builtins.newFunc(self.BaseStr), METHOD)
        self.BaseStr.getTable().insert("__iter__", self.newDataModelUrl("object.__iter__"), Builtins.newFunc(self.BaseStr), METHOD)
        str_methods_str = ["capitalize", "center", "decode", "encode", "expandtabs", "format", "index", "join", "ljust", "lower", "lstrip", "partition", "replace", "rfind", "rindex", "rjust", "rpartition", "rsplit", "rstrip", "strip", "swapcase", "title", "translate", "upper", "zfill"]
        for m in str_methods_str:
            self.BaseStr.getTable().insert(m, Builtins.newLibUrl("stdtypes.html#str." + m), Builtins.newFunc(self.BaseStr), METHOD)
        str_methods_num = ["count", "isalnum", "isalpha", "isdigit", "islower", "isspace", "istitle", "isupper", "find", "startswith", "endswith"]
        for m in str_methods_num:
            self.BaseStr.getTable().insert(m, Builtins.newLibUrl("stdtypes.html#str." + m), Builtins.newFunc(self.BaseNum), METHOD)
        str_methods_list = ["split", "splitlines"]
        for m in str_methods_list:
            self.BaseStr.getTable().insert(m, Builtins.newLibUrl("stdtypes.html#str." + m), Builtins.newFunc(Builtins.newList(self.BaseStr)), METHOD)
        self.BaseStr.getTable().insert("partition", Builtins.newLibUrl("stdtypes"), Builtins.newFunc(Builtins.newTuple(self.BaseStr)), METHOD)

    def buildModuleType(self):
        """ generated source for method buildModuleType """
        attrs = ["__doc__", "__file__", "__name__", "__package__"]
        for m in attrs:
            self.BaseModule.getTable().insert(m, self.newTutUrl("modules.html"), self.BaseStr, ATTRIBUTE)
        self.BaseModule.getTable().insert("__dict__", Builtins.newLibUrl("stdtypes", "modules"), Builtins.newDict(self.BaseStr, Builtins.getUnknown()), ATTRIBUTE)

    def buildDictType(self):
        """ generated source for method buildDictType """
        url = "datastructures.html#dictionaries"
        bt = self.BaseDict.getTable()
        bt.insert("__getitem__", self.newTutUrl(url), Builtins.newFunc(), METHOD)
        bt.insert("__iter__", self.newTutUrl(url), Builtins.newFunc(), METHOD)
        bt.insert("get", self.newTutUrl(url), Builtins.newFunc(), METHOD)
        bt.insert("items", self.newTutUrl(url), Builtins.newFunc(Builtins.newList(Builtins.newTuple(Builtins.getUnknown(), Builtins.getUnknown()))), METHOD)
        bt.insert("keys", self.newTutUrl(url), Builtins.newFunc(self.BaseList), METHOD)
        bt.insert("values", self.newTutUrl(url), Builtins.newFunc(self.BaseList), METHOD)
        dict_method_unknown = ["clear", "copy", "fromkeys", "get", "iteritems", "iterkeys", "itervalues", "pop", "popitem", "setdefault", "update"]
        for m in dict_method_unknown:
            bt.insert(m, self.newTutUrl(url), Builtins.newFunc(), METHOD)
        dict_method_num = ["has_key"]
        for m in dict_method_num:
            bt.insert(m, self.newTutUrl(url), Builtins.newFunc(self.BaseNum), METHOD)

    def buildFileType(self):
        """ generated source for method buildFileType """
        url = "stdtypes.html#bltin-file-objects"
        table = self.BaseFile.getTable()
        methods_unknown = ["__enter__", "__exit__", "__iter__", "flush", "readinto", "truncate"]
        for m in methods_unknown:
            table.insert(m, Builtins.newLibUrl(url), Builtins.newFunc(), METHOD)
        methods_str = ["next", "read", "readline"]
        for m in methods_str:
            table.insert(m, Builtins.newLibUrl(url), Builtins.newFunc(self.BaseStr), METHOD)
        num = ["fileno", "isatty", "tell"]
        for m in num:
            table.insert(m, Builtins.newLibUrl(url), Builtins.newFunc(self.BaseNum), METHOD)
        methods_none = ["close", "seek", "write", "writelines"]
        for m in methods_none:
            table.insert(m, Builtins.newLibUrl(url), Builtins.newFunc(self.None_), METHOD)
        table.insert("readlines", Builtins.newLibUrl(url), Builtins.newFunc(Builtins.newList(self.BaseStr)), METHOD)
        table.insert("xreadlines", Builtins.newLibUrl(url), Builtins.newFunc(self.BaseStr), METHOD)
        table.insert("closed", Builtins.newLibUrl(url), self.BaseNum, ATTRIBUTE)
        table.insert("encoding", Builtins.newLibUrl(url), self.BaseStr, ATTRIBUTE)
        table.insert("errors", Builtins.newLibUrl(url), Builtins.getUnknown(), ATTRIBUTE)
        table.insert("mode", Builtins.newLibUrl(url), self.BaseNum, ATTRIBUTE)
        table.insert("name", Builtins.newLibUrl(url), self.BaseStr, ATTRIBUTE)
        table.insert("softspace", Builtins.newLibUrl(url), self.BaseNum, ATTRIBUTE)
        table.insert("newlines", Builtins.newLibUrl(url), self.newUnion(self.BaseStr, Builtins.newTuple(self.BaseStr)), ATTRIBUTE)

    def buildFunctionType(self):
        from pysonarsq.java.Analyzer import Analyzer
        """ generated source for method buildFunctionType """
        t = self.BaseFunction.getTable()
        for s in Builtins.list_("func_doc", "__doc__", "func_name", "__name__", "__module__"):
            t.insert(s, Url(self.DATAMODEL_URL), self.BaseStr, ATTRIBUTE)
        t.insert("func_closure", Url(self.DATAMODEL_URL), Builtins.newTuple(), ATTRIBUTE)
        t.insert("func_code", Url(self.DATAMODEL_URL), Builtins.getUnknown(), ATTRIBUTE)
        t.insert("func_defaults", Url(self.DATAMODEL_URL), Builtins.newTuple(), ATTRIBUTE)
        t.insert("func_globals", Url(self.DATAMODEL_URL), DictType(self.BaseStr, Analyzer.self.builtins.unknown), ATTRIBUTE)
        t.insert("func_dict", Url(self.DATAMODEL_URL), DictType(self.BaseStr, Analyzer.self.builtins.unknown), ATTRIBUTE)
        #  Assume any function can become a method, for simplicity.
        for s in Builtins.list_("__func__", "im_func"):
            t.insert(s, Url(self.DATAMODEL_URL), FunType(), METHOD)

    #  XXX:  finish wiring this up.  ClassType needs to inherit from it somehow,
    #  so we can remove the per-instance attributes from NClassDef.
    def buildClassType(self):
        """ generated source for method buildClassType """
        t = self.BaseClass.getTable()
        for s in Builtins.list_("__name__", "__doc__", "__module__"):
            t.insert(s, Url(self.DATAMODEL_URL), self.BaseStr, ATTRIBUTE)
        t.insert("__dict__", Url(self.DATAMODEL_URL), DictType(self.BaseStr, Builtins.getUnknown()), ATTRIBUTE)

    class BuiltinsModule(NativeModule):
        """ generated source for class BuiltinsModule """
        def __init__(self, above_me):
            """ generated source for method __init__ """
            super(Builtins.BuiltinsModule, self).__init__("__builtin__")
            above_me.Builtin = module_ = Builtins.newModule(self.name)
            self.table = module_.getTable()

        def initBindings(self):
            from pysonarsq.java.Analyzer import Analyzer
            global self_instance
            
            Analyzer.self.moduleTable.insert(self.name, self.liburl(), self.getModule(), MODULE)
            self.table.addSuper(self_instance.BaseModule.getTable())
            self.addClass("None", Builtins.newLibUrl("constants"), self_instance.None_)
            self.addFunction("bool", Builtins.newLibUrl("functions", "bool"), self_instance.BaseBool)
            self.addFunction("complex", Builtins.newLibUrl("functions", "complex"), self_instance.BaseComplex)
            self.addClass("dict", Builtins.newLibUrl("stdtypes", "typesmapping"), self_instance.BaseDict)
            self.addFunction("file", Builtins.newLibUrl("functions", "file"), self_instance.BaseFileInst)
            self.addFunction("int", Builtins.newLibUrl("functions", "int"), self_instance.BaseNum)
            self.addFunction("long", Builtins.newLibUrl("functions", "long"), self_instance.BaseNum)
            self.addFunction("float", Builtins.newLibUrl("functions", "float"), self_instance.BaseFloat)
            self.addFunction("list", Builtins.newLibUrl("functions", "list"), InstanceType(self_instance.BaseList))
            self.addFunction("object", Builtins.newLibUrl("functions", "object"), InstanceType(self_instance.Object))
            self.addFunction("str", Builtins.newLibUrl("functions", "str"), self_instance.BaseStr)
            self.addFunction("tuple", Builtins.newLibUrl("functions", "tuple"), InstanceType(self_instance.BaseTuple))
            self.addFunction("type", Builtins.newLibUrl("functions", "type"), InstanceType(self_instance.Type))
            #  XXX:  need to model the following as built-in class types:
            #    basestring, bool, buffer, frozenset, property, set, slice,
            #    staticmethod, super and unicode
            builtin_func_unknown = ["apply", "basestring", "callable", "classmethod", "coerce", "compile", "copyright", "credits", "delattr", "enumerate", "eval", "execfile", "exit", "filter", "frozenset", "getattr", "help", "input", "intern", "iter", "license", "long", "property", "quit", "raw_input", "reduce", "reload", "reversed", "set", "setattr", "slice", "sorted", "staticmethod", "super", "type", "unichr", "unicode"]
            for f in builtin_func_unknown:
                self.addFunction(f, Builtins.newLibUrl("functions.html#" + f), Builtins.getUnknown())
            builtin_func_num = ["abs", "all", "any", "cmp", "coerce", "divmod", "hasattr", "hash", "id", "isinstance", "issubclass", "len", "max", "min", "ord", "pow", "round", "sum"]
            for f in builtin_func_num:
                self.addFunction(f, Builtins.newLibUrl("functions.html#" + f), self_instance.BaseNum)
            for f in Builtins.list_("hex", "oct", "repr", "chr"):
                self.addFunction(f, Builtins.newLibUrl("functions.html#" + f), self_instance.BaseStr)
            self.addFunction("dir", Builtins.newLibUrl("functions", "dir"), Builtins.newList(self_instance.BaseStr))
            self.addFunction("map", Builtins.newLibUrl("functions", "map"), Builtins.newList(Builtins.getUnknown()))
            self.addFunction("range", Builtins.newLibUrl("functions", "range"), Builtins.newList(self_instance.BaseNum))
            self.addFunction("xrange", Builtins.newLibUrl("functions", "range"), Builtins.newList(self_instance.BaseNum))
            self.addFunction("buffer", Builtins.newLibUrl("functions", "buffer"), Builtins.newList(Builtins.getUnknown()))
            self.addFunction("zip", Builtins.newLibUrl("functions", "zip"), Builtins.newList(Builtins.newTuple(Builtins.getUnknown())))
            
            for f in Builtins.list_("globals", "vars", "locals"):
                self.addFunction(f, Builtins.newLibUrl("functions.html#" + f), Builtins.newDict(self_instance.BaseStr, Builtins.getUnknown()))
                
            for f in self_instance.builtin_exception_types:
                self.addClass(f, Builtins.newDataModelUrl("org/yinwang/pysonar/types"), Builtins.newClass(f, Analyzer.self.globaltable, self_instance.Object))
                
            self.BaseException = self.table.lookupType("BaseException")
            
            for f in Builtins.list_("True", "False"):
                self.addAttr(f, Builtins.newDataModelUrl("org/yinwang/pysonar/types"), self_instance.BaseBool)
                
            self.addAttr("None", Builtins.newDataModelUrl("org/yinwang/pysonar/types"), self_instance.None_)
            self.addFunction("open", Builtins.newTutUrl("inputoutput.html#reading-and-writing-files"), self_instance.BaseFileInst)
            self.addFunction("__import__", Builtins.newLibUrl("functions"), Builtins.newModule("<?>"))
            Analyzer.self.globaltable.insert("__builtins__", self.liburl(), self.module_, ATTRIBUTE)
            Analyzer.self.globaltable.putAll(self.table)

    class ArrayModule(NativeModule):
        """ generated source for class ArrayModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ArrayModule, self).__init__("array")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("array", Builtins.newLibUrl("array", "array"), self.BaseArray)
            addClass("ArrayType", Builtins.newLibUrl("array", "ArrayType"), self.BaseArray)

    class AudioopModule(NativeModule):
        """ generated source for class AudioopModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.AudioopModule, self).__init__("audioop")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("error", liburl(), self.newException("error", table))
            addStrFuncs("add", "adpcm2lin", "alaw2lin", "bias", "lin2alaw", "lin2lin", "lin2ulaw", "mul", "reverse", "tomono", "ulaw2lin")
            addNumFuncs("avg", "avgpp", "cross", "findfactor", "findmax", "getsample", "max", "maxpp", "rms")
            for s in Builtins.list_("adpcm2lin", "findfit", "lin2adpcm", "minmax", "ratecv"):
                addFunction(s, liburl(), Builtins.newTuple())

    class BinasciiModule(NativeModule):
        """ generated source for class BinasciiModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.BinasciiModule, self).__init__("binascii")

        def initBindings(self):
            """ generated source for method initBindings """
            addStrFuncs("a2b_uu", "b2a_uu", "a2b_base64", "b2a_base64", "a2b_qp", "b2a_qp", "a2b_hqx", "rledecode_hqx", "rlecode_hqx", "b2a_hqx", "b2a_hex", "hexlify", "a2b_hex", "unhexlify")
            addNumFuncs("crc_hqx", "crc32")
            addClass("Error", liburl(), self.newException("Error", table))
            addClass("Incomplete", liburl(), self.newException("Incomplete", table))

    class Bz2Module(NativeModule):
        """ generated source for class Bz2Module """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.Bz2Module, self).__init__("bz2")

        def initBindings(self):
            """ generated source for method initBindings """
            bz2 = Builtins.newClass("BZ2File", table, self.BaseFile)
            #  close enough.
            addClass("BZ2File", liburl(), bz2)
            bz2c = Builtins.newClass("BZ2Compressor", table, self.Object)
            bz2c.getTable().insert("compress", Builtins.newLibUrl("bz2", "sequential-de-compression"), Builtins.newFunc(self.BaseStr), METHOD)
            bz2c.getTable().insert("flush", Builtins.newLibUrl("bz2", "sequential-de-compression"), Builtins.newFunc(self.None_), METHOD)
            addClass("BZ2Compressor", Builtins.newLibUrl("bz2", "sequential-de-compression"), bz2c)
            bz2d = Builtins.newClass("BZ2Decompressor", table, self.Object)
            bz2d.getTable().insert("decompress", Builtins.newLibUrl("bz2", "sequential-de-compression"), Builtins.newFunc(self.BaseStr), METHOD)
            addClass("BZ2Decompressor", Builtins.newLibUrl("bz2", "sequential-de-compression"), bz2d)
            addFunction("compress", Builtins.newLibUrl("bz2", "one-shot-de-compression"), self.BaseStr)
            addFunction("decompress", Builtins.newLibUrl("bz2", "one-shot-de-compression"), self.BaseStr)

    class CPickleModule(NativeModule):
        """ generated source for class CPickleModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.CPickleModule, self).__init__("cPickle")

        def liburl(self):
            """ generated source for method liburl """
            return Builtins.newLibUrl("pickle", "module-cPickle")

        def initBindings(self):
            """ generated source for method initBindings """
            addUnknownFuncs("dump", "load", "dumps", "loads")
            addClass("PickleError", self.liburl(), self.newException("PickleError", table))
            picklingError = self.newException("PicklingError", table)
            addClass("PicklingError", self.liburl(), picklingError)
            update("UnpickleableError", self.liburl(), Builtins.newClass("UnpickleableError", table, picklingError), CLASS)
            unpicklingError = self.newException("UnpicklingError", table)
            addClass("UnpicklingError", self.liburl(), unpicklingError)
            update("BadPickleGet", self.liburl(), Builtins.newClass("BadPickleGet", table, unpicklingError), CLASS)
            pickler = Builtins.newClass("Pickler", table, self.Object)
            pickler.getTable().insert("dump", self.liburl(), Builtins.newFunc(), METHOD)
            pickler.getTable().insert("clear_memo", self.liburl(), Builtins.newFunc(), METHOD)
            addClass("Pickler", self.liburl(), pickler)
            unpickler = Builtins.newClass("Unpickler", table, self.Object)
            unpickler.getTable().insert("load", self.liburl(), Builtins.newFunc(), METHOD)
            unpickler.getTable().insert("noload", self.liburl(), Builtins.newFunc(), METHOD)
            addClass("Unpickler", self.liburl(), unpickler)

    class CStringIOModule(NativeModule):
        """ generated source for class CStringIOModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.CStringIOModule, self).__init__("cStringIO")

        #@overloaded
        def liburl(self, anchor=None):
            """ generated source for method liburl """
            return Builtins.newLibUrl("stringio", anchor)

        def initBindings(self):
            """ generated source for method initBindings """
            StringIO = Builtins.newClass("StringIO", table, self.BaseFile)
            addFunction("StringIO", self.liburl(), InstanceType(StringIO))
            addAttr("InputType", self.liburl(), self.Type)
            addAttr("OutputType", self.liburl(), self.Type)
            addAttr("cStringIO_CAPI", self.liburl(), Builtins.getUnknown())

    class CMathModule(NativeModule):
        """ generated source for class CMathModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.CMathModule, self).__init__("cmath")

        def initBindings(self):
            """ generated source for method initBindings """
            addFunction("phase", liburl("conversions-to-and-from-polar-coordinates"), self.BaseNum)
            addFunction("polar", liburl("conversions-to-and-from-polar-coordinates"), Builtins.newTuple(self.BaseNum, self.BaseNum))
            addFunction("rect", liburl("conversions-to-and-from-polar-coordinates"), self.BaseComplex)
            for plf in Builtins.list_("exp", "log", "log10", "sqrt"):
                addFunction(plf, liburl("power-and-logarithmic-functions"), self.BaseNum)
            for tf in Builtins.list_("acos", "asin", "atan", "cos", "sin", "tan"):
                addFunction(tf, liburl("trigonometric-functions"), self.BaseNum)
            for hf in Builtins.list_("acosh", "asinh", "atanh", "cosh", "sinh", "tanh"):
                addFunction(hf, liburl("hyperbolic-functions"), self.BaseComplex)
            for cf in Builtins.list_("isinf", "isnan"):
                addFunction(cf, liburl("classification-functions"), self.BaseBool)
            for c in Builtins.list_("pi", "e"):
                addAttr(c, liburl("constants"), self.BaseNum)

    class CollectionsModule(NativeModule):
        """ generated source for class CollectionsModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.CollectionsModule, self).__init__("collections")

        def abcUrl(self):
            """ generated source for method abcUrl """
            return liburl("abcs-abstract-base-classes")

        def dequeUrl(self):
            """ generated source for method dequeUrl """
            return liburl("deque-objects")

        def initBindings(self):
            """ generated source for method initBindings """
            Callable = Builtins.newClass("Callable", table, self.Object)
            Callable.getTable().insert("__call__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("Callable", self.abcUrl(), Callable)
            Iterable = Builtins.newClass("Iterable", table, self.Object)
            Iterable.getTable().insert("__next__", self.abcUrl(), Builtins.newFunc(), METHOD)
            Iterable.getTable().insert("__iter__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("Iterable", self.abcUrl(), Iterable)
            Hashable = Builtins.newClass("Hashable", table, self.Object)
            Hashable.getTable().insert("__hash__", self.abcUrl(), Builtins.newFunc(self.BaseNum), METHOD)
            addClass("Hashable", self.abcUrl(), Hashable)
            Sized = Builtins.newClass("Sized", table, self.Object)
            Sized.getTable().insert("__len__", self.abcUrl(), Builtins.newFunc(self.BaseNum), METHOD)
            addClass("Sized", self.abcUrl(), Sized)
            Container = Builtins.newClass("Container", table, self.Object)
            Container.getTable().insert("__contains__", self.abcUrl(), Builtins.newFunc(self.BaseNum), METHOD)
            addClass("Container", self.abcUrl(), Container)
            Iterator = Builtins.newClass("Iterator", table, Iterable)
            addClass("Iterator", self.abcUrl(), Iterator)
            Sequence = Builtins.newClass("Sequence", table, Sized, Iterable, Container)
            Sequence.getTable().insert("__getitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            Sequence.getTable().insert("reversed", self.abcUrl(), Builtins.newFunc(Sequence), METHOD)
            Sequence.getTable().insert("index", self.abcUrl(), Builtins.newFunc(self.BaseNum), METHOD)
            Sequence.getTable().insert("count", self.abcUrl(), Builtins.newFunc(self.BaseNum), METHOD)
            addClass("Sequence", self.abcUrl(), Sequence)
            MutableSequence = Builtins.newClass("MutableSequence", table, Sequence)
            MutableSequence.getTable().insert("__setitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            MutableSequence.getTable().insert("__delitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("MutableSequence", self.abcUrl(), MutableSequence)
            Set = Builtins.newClass("Set", table, Sized, Iterable, Container)
            Set.getTable().insert("__getitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("Set", self.abcUrl(), Set)
            MutableSet = Builtins.newClass("MutableSet", table, Set)
            MutableSet.getTable().insert("add", self.abcUrl(), Builtins.newFunc(), METHOD)
            MutableSet.getTable().insert("discard", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("MutableSet", self.abcUrl(), MutableSet)
            Mapping = Builtins.newClass("Mapping", table, Sized, Iterable, Container)
            Mapping.getTable().insert("__getitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("Mapping", self.abcUrl(), Mapping)
            MutableMapping = Builtins.newClass("MutableMapping", table, Mapping)
            MutableMapping.getTable().insert("__setitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            MutableMapping.getTable().insert("__delitem__", self.abcUrl(), Builtins.newFunc(), METHOD)
            addClass("MutableMapping", self.abcUrl(), MutableMapping)
            MappingView = Builtins.newClass("MappingView", table, Sized)
            addClass("MappingView", self.abcUrl(), MappingView)
            KeysView = Builtins.newClass("KeysView", table, Sized)
            addClass("KeysView", self.abcUrl(), KeysView)
            ItemsView = Builtins.newClass("ItemsView", table, Sized)
            addClass("ItemsView", self.abcUrl(), ItemsView)
            ValuesView = Builtins.newClass("ValuesView", table, Sized)
            addClass("ValuesView", self.abcUrl(), ValuesView)
            deque = Builtins.newClass("deque", table, self.Object)
            for n in Builtins.list_("append", "appendLeft", "clear", "extend", "extendLeft", "rotate"):
                deque.getTable().insert(n, self.dequeUrl(), Builtins.newFunc(self.None_), METHOD)
            for u in Builtins.list_("__getitem__", "__iter__", "pop", "popleft", "remove"):
                deque.getTable().insert(u, self.dequeUrl(), Builtins.newFunc(), METHOD)
            addClass("deque", self.dequeUrl(), deque)
            defaultdict = Builtins.newClass("defaultdict", table, self.Object)
            defaultdict.getTable().insert("__missing__", liburl("defaultdict-objects"), Builtins.newFunc(), METHOD)
            defaultdict.getTable().insert("default_factory", liburl("defaultdict-objects"), Builtins.newFunc(), METHOD)
            addClass("defaultdict", liburl("defaultdict-objects"), defaultdict)
            argh = "namedtuple-factory-function-for-tuples-with-named-fields"
            namedtuple = Builtins.newClass("(namedtuple)", table, self.BaseTuple)
            namedtuple.getTable().insert("_fields", liburl(argh), ListType(self.BaseStr), ATTRIBUTE)
            addFunction("namedtuple", liburl(argh), namedtuple)

    class CTypesModule(NativeModule):
        """ generated source for class CTypesModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.CTypesModule, self).__init__("ctypes")

        def initBindings(self):
            """ generated source for method initBindings """
            ctypes_attrs = ["ARRAY", "ArgumentError", "Array", "BigEndianStructure", "CDLL", "CFUNCTYPE", "DEFAULT_MODE", "DllCanUnloadNow", "DllGetClassObject", "FormatError", "GetLastError", "HRESULT", "LibraryLoader", "LittleEndianStructure", "OleDLL", "POINTER", "PYFUNCTYPE", "PyDLL", "RTLD_GLOBAL", "RTLD_LOCAL", "SetPointerType", "Structure", "Union", "WINFUNCTYPE", "WinDLL", "WinError", "_CFuncPtr", "_FUNCFLAG_CDECL", "_FUNCFLAG_PYTHONAPI", "_FUNCFLAG_STDCALL", "_FUNCFLAG_USE_ERRNO", "_FUNCFLAG_USE_LASTERROR", "_Pointer", "_SimpleCData", "_c_functype_cache", "_calcsize", "_cast", "_cast_addr", "_check_HRESULT", "_check_size", "_ctypes_version", "_dlopen", "_endian", "_memmove_addr", "_memset_addr", "_os", "_pointer_type_cache", "_string_at", "_string_at_addr", "_sys", "_win_functype_cache", "_wstring_at", "_wstring_at_addr", "addressof", "alignment", "byref", "c_bool", "c_buffer", "c_byte", "c_char", "c_char_p", "c_double", "c_float", "c_int", "c_int16", "c_int32", "c_int64", "c_int8", "c_long", "c_longdouble", "c_longlong", "c_short", "c_size_t", "c_ubyte", "c_uint", "c_uint16", "c_uint32", "c_uint64", "c_uint8", "c_ulong", "c_ulonglong", "c_ushort", "c_void_p", "c_voidp", "c_wchar", "c_wchar_p", "cast", "cdll", "create_string_buffer", "create_unicode_buffer", "get_errno", "get_last_error", "memmove", "memset", "oledll", "pointer", "py_object", "pydll", "pythonapi", "resize", "set_conversion_mode", "set_errno", "set_last_error", "sizeof", "string_at", "windll", "wstring_at"]
            for attr in ctypes_attrs:
                addAttr(attr, liburl(attr), Builtins.getUnknown())

    class CryptModule(NativeModule):
        def __init__(self):
            super(Builtins.CryptModule, self).__init__("crypt")

        def initBindings(self):
            addStrFuncs("crypt")

    class DatetimeModule(NativeModule):
        def __init__(self):
            super(Builtins.DatetimeModule, self).__init__("datetime")

        def dtUrl(self, anchor):
            return liburl("datetime." + anchor)

        def initBindings(self):
            #  XXX:  make datetime, time, date, timedelta and tzinfo Base* objects,
            #  so built-in functions can return them.
            self.addNumAttrs("MINYEAR", "MAXYEAR")
            timedelta = self.Datetime_timedelta = Builtins.newClass("timedelta", self.table, self.Object)
            addClass("timedelta", self.dtUrl("timedelta"), timedelta)
            tdtable = self.Datetime_timedelta.getTable()
            tdtable.insert("min", self.dtUrl("timedelta"), timedelta, ATTRIBUTE)
            tdtable.insert("max", self.dtUrl("timedelta"), timedelta, ATTRIBUTE)
            tdtable.insert("resolution", self.dtUrl("timedelta"), timedelta, ATTRIBUTE)
            tdtable.insert("days", self.dtUrl("timedelta"), self.BaseNum, ATTRIBUTE)
            tdtable.insert("seconds", self.dtUrl("timedelta"), self.BaseNum, ATTRIBUTE)
            tdtable.insert("microseconds", self.dtUrl("timedelta"), self.BaseNum, ATTRIBUTE)
            tzinfo = self.Datetime_tzinfo = Builtins.newClass("tzinfo", table, self.Object)
            addClass("tzinfo", self.dtUrl("tzinfo"), tzinfo)
            tztable = self.Datetime_tzinfo.getTable()
            tztable.insert("utcoffset", self.dtUrl("tzinfo"), Builtins.newFunc(timedelta), METHOD)
            tztable.insert("dst", self.dtUrl("tzinfo"), Builtins.newFunc(timedelta), METHOD)
            tztable.insert("tzname", self.dtUrl("tzinfo"), Builtins.newFunc(self.BaseStr), METHOD)
            tztable.insert("fromutc", self.dtUrl("tzinfo"), Builtins.newFunc(tzinfo), METHOD)
            date = self.Datetime_date = Builtins.newClass("date", table, self.Object)
            addClass("date", self.dtUrl("date"), date)
            dtable = self.Datetime_date.getTable()
            dtable.insert("min", self.dtUrl("date"), date, ATTRIBUTE)
            dtable.insert("max", self.dtUrl("date"), date, ATTRIBUTE)
            dtable.insert("resolution", self.dtUrl("date"), timedelta, ATTRIBUTE)
            dtable.insert("today", self.dtUrl("date"), Builtins.newFunc(date), METHOD)
            dtable.insert("fromtimestamp", self.dtUrl("date"), Builtins.newFunc(date), METHOD)
            dtable.insert("fromordinal", self.dtUrl("date"), Builtins.newFunc(date), METHOD)
            dtable.insert("year", self.dtUrl("date"), self.BaseNum, ATTRIBUTE)
            dtable.insert("month", self.dtUrl("date"), self.BaseNum, ATTRIBUTE)
            dtable.insert("day", self.dtUrl("date"), self.BaseNum, ATTRIBUTE)
            dtable.insert("replace", self.dtUrl("date"), Builtins.newFunc(date), METHOD)
            dtable.insert("timetuple", self.dtUrl("date"), Builtins.newFunc(self.Time_struct_time), METHOD)
            for n in Builtins.list_("toordinal", "weekday", "isoweekday"):
                dtable.insert(n, self.dtUrl("date"), Builtins.newFunc(self.BaseNum), METHOD)
            for r in Builtins.list_("ctime", "strftime", "isoformat"):
                dtable.insert(r, self.dtUrl("date"), Builtins.newFunc(self.BaseStr), METHOD)
            dtable.insert("isocalendar", self.dtUrl("date"), Builtins.newFunc(Builtins.newTuple(self.BaseNum, self.BaseNum, self.BaseNum)), METHOD)
            time = self.Datetime_time = Builtins.newClass("time", table, self.Object)
            addClass("time", self.dtUrl("time"), date)
            ttable = self.Datetime_time.getTable()
            ttable.insert("min", self.dtUrl("time"), time, ATTRIBUTE)
            ttable.insert("max", self.dtUrl("time"), time, ATTRIBUTE)
            ttable.insert("resolution", self.dtUrl("time"), timedelta, ATTRIBUTE)
            ttable.insert("hour", self.dtUrl("time"), self.BaseNum, ATTRIBUTE)
            ttable.insert("minute", self.dtUrl("time"), self.BaseNum, ATTRIBUTE)
            ttable.insert("second", self.dtUrl("time"), self.BaseNum, ATTRIBUTE)
            ttable.insert("microsecond", self.dtUrl("time"), self.BaseNum, ATTRIBUTE)
            ttable.insert("tzinfo", self.dtUrl("time"), tzinfo, ATTRIBUTE)
            ttable.insert("replace", self.dtUrl("time"), Builtins.newFunc(time), METHOD)
            for l in Builtins.list_("isoformat", "strftime", "tzname"):
                ttable.insert(l, self.dtUrl("time"), Builtins.newFunc(self.BaseStr), METHOD)
            for f in Builtins.list_("utcoffset", "dst"):
                ttable.insert(f, self.dtUrl("time"), Builtins.newFunc(timedelta), METHOD)
            datetime = self.Datetime_datetime = Builtins.newClass("datetime", table, date, time)
            addClass("datetime", self.dtUrl("datetime"), datetime)
            dttable = self.Datetime_datetime.getTable()
            for c in Builtins.list_("combine", "fromordinal", "fromtimestamp", "now", "strptime", "today", "utcfromtimestamp", "utcnow"):
                dttable.insert(c, self.dtUrl("datetime"), Builtins.newFunc(datetime), METHOD)
            dttable.insert("min", self.dtUrl("datetime"), datetime, ATTRIBUTE)
            dttable.insert("max", self.dtUrl("datetime"), datetime, ATTRIBUTE)
            dttable.insert("resolution", self.dtUrl("datetime"), timedelta, ATTRIBUTE)
            dttable.insert("date", self.dtUrl("datetime"), Builtins.newFunc(date), METHOD)
            for x in Builtins.list_("time", "timetz"):
                dttable.insert(x, self.dtUrl("datetime"), Builtins.newFunc(time), METHOD)
            for y in Builtins.list_("replace", "astimezone"):
                dttable.insert(y, self.dtUrl("datetime"), Builtins.newFunc(datetime), METHOD)
            dttable.insert("utctimetuple", self.dtUrl("datetime"), Builtins.newFunc(self.Time_struct_time), METHOD)

    class DbmModule(NativeModule):
        def __init__(self):
            super(Builtins.DbmModule, self).__init__("dbm")

        def initBindings(self):
            """ generated source for method initBindings """
            dbm = ClassType("dbm", table, self.BaseDict)
            addClass("dbm", liburl(), dbm)
            addClass("error", liburl(), self.newException("error", table))
            addStrAttrs("library")
            addFunction("open", liburl(), dbm)

    class ErrnoModule(NativeModule):
        """ generated source for class ErrnoModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ErrnoModule, self).__init__("errno")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumAttrs("E2BIG", "EACCES", "EADDRINUSE", "EADDRNOTAVAIL", "EAFNOSUPPORT", "EAGAIN", "EALREADY", "EBADF", "EBUSY", "ECHILD", "ECONNABORTED", "ECONNREFUSED", "ECONNRESET", "EDEADLK", "EDEADLOCK", "EDESTADDRREQ", "EDOM", "EDQUOT", "EEXIST", "EFAULT", "EFBIG", "EHOSTDOWN", "EHOSTUNREACH", "EILSEQ", "EINPROGRESS", "EINTR", "EINVAL", "EIO", "EISCONN", "EISDIR", "ELOOP", "EMFILE", "EMLINK", "EMSGSIZE", "ENAMETOOLONG", "ENETDOWN", "ENETRESET", "ENETUNREACH", "ENFILE", "ENOBUFS", "ENODEV", "ENOENT", "ENOEXEC", "ENOLCK", "ENOMEM", "ENOPROTOOPT", "ENOSPC", "ENOSYS", "ENOTCONN", "ENOTDIR", "ENOTEMPTY", "ENOTSOCK", "ENOTTY", "ENXIO", "EOPNOTSUPP", "EPERM", "EPFNOSUPPORT", "EPIPE", "EPROTONOSUPPORT", "EPROTOTYPE", "ERANGE", "EREMOTE", "EROFS", "ESHUTDOWN", "ESOCKTNOSUPPORT", "ESPIPE", "ESRCH", "ESTALE", "ETIMEDOUT", "ETOOMANYREFS", "EUSERS", "EWOULDBLOCK", "EXDEV", "WSABASEERR", "WSAEACCES", "WSAEADDRINUSE", "WSAEADDRNOTAVAIL", "WSAEAFNOSUPPORT", "WSAEALREADY", "WSAEBADF", "WSAECONNABORTED", "WSAECONNREFUSED", "WSAECONNRESET", "WSAEDESTADDRREQ", "WSAEDISCON", "WSAEDQUOT", "WSAEFAULT", "WSAEHOSTDOWN", "WSAEHOSTUNREACH", "WSAEINPROGRESS", "WSAEINTR", "WSAEINVAL", "WSAEISCONN", "WSAELOOP", "WSAEMFILE", "WSAEMSGSIZE", "WSAENAMETOOLONG", "WSAENETDOWN", "WSAENETRESET", "WSAENETUNREACH", "WSAENOBUFS", "WSAENOPROTOOPT", "WSAENOTCONN", "WSAENOTEMPTY", "WSAENOTSOCK", "WSAEOPNOTSUPP", "WSAEPFNOSUPPORT", "WSAEPROCLIM", "WSAEPROTONOSUPPORT", "WSAEPROTOTYPE", "WSAEREMOTE", "WSAESHUTDOWN", "WSAESOCKTNOSUPPORT", "WSAESTALE", "WSAETIMEDOUT", "WSAETOOMANYREFS", "WSAEUSERS", "WSAEWOULDBLOCK", "WSANOTINITIALISED", "WSASYSNOTREADY", "WSAVERNOTSUPPORTED")
            addAttr("errorcode", liburl("errorcode"), Builtins.newDict(self.BaseNum, self.BaseStr))

    class ExceptionsModule(NativeModule):
        """ generated source for class ExceptionsModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ExceptionsModule, self).__init__("exceptions")

        def initBindings(self):
            """ generated source for method initBindings """
            builtins = self.get("__builtin__")
            for s in builtin_exception_types:
                pass
                #                 Binding b = builtins.getTable().lookup(s);
                #                 table.update(b.__name__, b.getFirstNode(), b.getType(), b.getKind());

    class FcntlModule(NativeModule):
        """ generated source for class FcntlModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.FcntlModule, self).__init__("fcntl")

        def initBindings(self):
            """ generated source for method initBindings """
            for s in Builtins.list_("fcntl", "ioctl"):
                addFunction(s, liburl(), self.newUnion(self.BaseNum, self.BaseStr))
            addNumFuncs("flock")
            addUnknownFuncs("lockf")
            addNumAttrs("DN_ACCESS", "DN_ATTRIB", "DN_CREATE", "DN_DELETE", "DN_MODIFY", "DN_MULTISHOT", "DN_RENAME", "FASYNC", "FD_CLOEXEC", "F_DUPFD", "F_EXLCK", "F_GETFD", "F_GETFL", "F_GETLEASE", "F_GETLK", "F_GETLK64", "F_GETOWN", "F_GETSIG", "F_NOTIFY", "F_RDLCK", "F_SETFD", "F_SETFL", "F_SETLEASE", "F_SETLK", "F_SETLK64", "F_SETLKW", "F_SETLKW64", "F_SETOWN", "F_SETSIG", "F_SHLCK", "F_UNLCK", "F_WRLCK", "I_ATMARK", "I_CANPUT", "I_CKBAND", "I_FDINSERT", "I_FIND", "I_FLUSH", "I_FLUSHBAND", "I_GETBAND", "I_GETCLTIME", "I_GETSIG", "I_GRDOPT", "I_GWROPT", "I_LINK", "I_LIST", "I_LOOK", "I_NREAD", "I_PEEK", "I_PLINK", "I_POP", "I_PUNLINK", "I_PUSH", "I_RECVFD", "I_SENDFD", "I_SETCLTIME", "I_SETSIG", "I_SRDOPT", "I_STR", "I_SWROPT", "I_UNLINK", "LOCK_EX", "LOCK_MAND", "LOCK_NB", "LOCK_READ", "LOCK_RW", "LOCK_SH", "LOCK_UN", "LOCK_WRITE")

    class FpectlModule(NativeModule):
        """ generated source for class FpectlModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.FpectlModule, self).__init__("fpectl")

        def initBindings(self):
            """ generated source for method initBindings """
            addNoneFuncs("turnon_sigfpe", "turnoff_sigfpe")
            addClass("FloatingPointError", liburl(), self.newException("FloatingPointError", table))

    class GcModule(NativeModule):
        """ generated source for class GcModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.GcModule, self).__init__("gc")

        def initBindings(self):
            """ generated source for method initBindings """
            addNoneFuncs("enable", "disable", "set_debug", "set_threshold")
            addNumFuncs("isenabled", "collect", "get_debug", "get_count", "get_threshold")
            for s in Builtins.list_("get_objects", "get_referrers", "get_referents"):
                addFunction(s, liburl(), Builtins.newList())
            addAttr("garbage", liburl(), Builtins.newList())
            addNumAttrs("DEBUG_STATS", "DEBUG_COLLECTABLE", "DEBUG_UNCOLLECTABLE", "DEBUG_INSTANCES", "DEBUG_OBJECTS", "DEBUG_SAVEALL", "DEBUG_LEAK")

    class GdbmModule(NativeModule):
        """ generated source for class GdbmModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.GdbmModule, self).__init__("gdbm")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("error", liburl(), self.newException("error", table))
            gdbm = ClassType("gdbm", table, self.BaseDict)
            gdbm.getTable().insert("firstkey", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            gdbm.getTable().insert("nextkey", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            gdbm.getTable().insert("reorganize", liburl(), Builtins.newFunc(self.None_), METHOD)
            gdbm.getTable().insert("sync", liburl(), Builtins.newFunc(self.None_), METHOD)
            addFunction("open", liburl(), gdbm)

    class GrpModule(NativeModule):
        """ generated source for class GrpModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.GrpModule, self).__init__("grp")

        def initBindings(self):
            """ generated source for method initBindings """
            Builtins.self.get("struct")
            struct_group = Builtins.newClass("struct_group", table, self.BaseStruct)
            struct_group.getTable().insert("gr_name", liburl(), self.BaseStr, ATTRIBUTE)
            struct_group.getTable().insert("gr_passwd", liburl(), self.BaseStr, ATTRIBUTE)
            struct_group.getTable().insert("gr_gid", liburl(), self.BaseNum, ATTRIBUTE)
            struct_group.getTable().insert("gr_mem", liburl(), Builtins.newList(self.BaseStr), ATTRIBUTE)
            addClass("struct_group", liburl(), struct_group)
            for s in Builtins.list_("getgrgid", "getgrnam"):
                addFunction(s, liburl(), struct_group)
            addFunction("getgrall", liburl(), ListType(struct_group))

    class ImpModule(NativeModule):
        """ generated source for class ImpModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ImpModule, self).__init__("imp")

        def initBindings(self):
            """ generated source for method initBindings """
            addStrFuncs("get_magic")
            addFunction("get_suffixes", liburl(), Builtins.newList(Builtins.newTuple(self.BaseStr, self.BaseStr, self.BaseNum)))
            addFunction("find_module", liburl(), Builtins.newTuple(self.BaseStr, self.BaseStr, self.BaseNum))
            module_methods = ["load_module", "new_module", "init_builtin", "init_frozen", "load_compiled", "load_dynamic", "load_source"]
            for mm in module_methods:
                addFunction(mm, liburl(), Builtins.newModule("<?>"))
            addUnknownFuncs("acquire_lock", "release_lock")
            addNumAttrs("PY_SOURCE", "PY_COMPILED", "C_EXTENSION", "PKG_DIRECTORY", "C_BUILTIN", "PY_FROZEN", "SEARCH_ERROR")
            addNumFuncs("lock_held", "is_builtin", "is_frozen")
            impNullImporter = Builtins.newClass("NullImporter", table, self.Object)
            impNullImporter.getTable().insert("find_module", liburl(), Builtins.newFunc(self.None_), FUNCTION)
            addClass("NullImporter", liburl(), impNullImporter)

    class ItertoolsModule(NativeModule):
        """ generated source for class ItertoolsModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ItertoolsModule, self).__init__("itertools")

        def initBindings(self):
            """ generated source for method initBindings """
            iterator = Builtins.newClass("iterator", table, self.Object)
            iterator.getTable().insert("from_iterable", liburl("itertool-functions"), Builtins.newFunc(iterator), METHOD)
            iterator.getTable().insert("next", liburl(), Builtins.newFunc(), METHOD)
            for s in Builtins.list_("chain", "combinations", "count", "cycle", "dropwhile", "groupby", "ifilter", "ifilterfalse", "imap", "islice", "izip", "izip_longest", "permutations", "product", "repeat", "starmap", "takewhile", "tee"):
                addClass(s, liburl("itertool-functions"), iterator)

    class MarshalModule(NativeModule):
        """ generated source for class MarshalModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.MarshalModule, self).__init__("marshal")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumAttrs("version")
            addStrFuncs("dumps")
            addUnknownFuncs("dump", "load", "loads")

    class MathModule(NativeModule):
        """ generated source for class MathModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.MathModule, self).__init__("math")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumFuncs("acos", "acosh", "asin", "asinh", "atan", "atan2", "atanh", "ceil", "copysign", "cos", "cosh", "degrees", "exp", "fabs", "factorial", "floor", "fmod", "frexp", "fsum", "hypot", "isinf", "isnan", "ldexp", "log", "log10", "log1p", "modf", "pow", "radians", "sin", "sinh", "sqrt", "tan", "tanh", "trunc")
            addNumAttrs("pi", "e")

    class Md5Module(NativeModule):
        """ generated source for class Md5Module """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.Md5Module, self).__init__("md5")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumAttrs("blocksize", "digest_size")
            md5 = Builtins.newClass("md5", table, self.Object)
            md5.getTable().insert("update", liburl(), Builtins.newFunc(), METHOD)
            md5.getTable().insert("digest", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            md5.getTable().insert("hexdigest", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            md5.getTable().insert("copy", liburl(), Builtins.newFunc(md5), METHOD)
            update("new", liburl(), Builtins.newFunc(md5), CONSTRUCTOR)
            update("md5", liburl(), Builtins.newFunc(md5), CONSTRUCTOR)

    class MmapModule(NativeModule):
        """ generated source for class MmapModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.MmapModule, self).__init__("mmap")

        def initBindings(self):
            """ generated source for method initBindings """
            mmap = Builtins.newClass("mmap", table, self.Object)
            for s in Builtins.list_("ACCESS_COPY", "ACCESS_READ", "ACCESS_WRITE", "ALLOCATIONGRANULARITY", "MAP_ANON", "MAP_ANONYMOUS", "MAP_DENYWRITE", "MAP_EXECUTABLE", "MAP_PRIVATE", "MAP_SHARED", "PAGESIZE", "PROT_EXEC", "PROT_READ", "PROT_WRITE"):
                mmap.getTable().insert(s, liburl(), self.BaseNum, ATTRIBUTE)
            for fstr in Builtins.list_("read", "read_byte", "readline"):
                mmap.getTable().insert(fstr, liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            for fnum in Builtins.list_("find", "rfind", "tell"):
                mmap.getTable().insert(fnum, liburl(), Builtins.newFunc(self.BaseNum), METHOD)
            for fnone in Builtins.list_("close", "flush", "move", "resize", "seek", "write", "write_byte"):
                mmap.getTable().insert(fnone, liburl(), Builtins.newFunc(self.None_), METHOD)
            addClass("mmap", liburl(), mmap)

    class NisModule(NativeModule):
        """ generated source for class NisModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.NisModule, self).__init__("nis")

        def initBindings(self):
            """ generated source for method initBindings """
            addStrFuncs("match", "cat", "get_default_domain")
            addFunction("maps", liburl(), Builtins.newList(self.BaseStr))
            addClass("error", liburl(), self.newException("error", table))

    class OsModule(NativeModule):
        """ generated source for class OsModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.OsModule, self).__init__("os")

        def initBindings(self):
            """ generated source for method initBindings """
            addAttr("name", liburl(), self.BaseStr)
            addClass("error", liburl(), self.newException("error", table))
            #  XXX: OSError
            initProcBindings()
            initProcMgmtBindings()
            initFileBindings()
            initFileAndDirBindings()
            initMiscSystemInfo()
            initOsPathModule()
            addAttr("errno", liburl(), Builtins.newModule("errno"))
            addFunction("urandom", liburl("miscellaneous-functions"), self.BaseStr)
            addAttr("NGROUPS_MAX", liburl(), self.BaseNum)
            for s in Builtins.list_("_Environ", "_copy_reg", "_execvpe", "_exists", "_get_exports_list", "_make_stat_result", "_make_statvfs_result", "_pickle_stat_result", "_pickle_statvfs_result", "_spawnvef"):
                addFunction(s, liburl(), Builtins.getUnknown())

        def initProcBindings(self):
            """ generated source for method initProcBindings """
            a = "process-parameters"
            addAttr("environ", liburl(a), Builtins.newDict(self.BaseStr, self.BaseStr))
            for s in Builtins.list_("chdir", "fchdir", "putenv", "setegid", "seteuid", "setgid", "setgroups", "setpgrp", "setpgid", "setreuid", "setregid", "setuid", "unsetenv"):
                addFunction(s, liburl(a), self.None_)
            for s in Builtins.list_("getegid", "getgid", "getpgid", "getpgrp", "getppid", "getuid", "getsid", "umask"):
                addFunction(s, liburl(a), self.BaseNum)
            for s in Builtins.list_("getcwd", "ctermid", "getlogin", "getenv", "strerror"):
                addFunction(s, liburl(a), self.BaseStr)
            addFunction("getgroups", liburl(a), Builtins.newList(self.BaseStr))
            addFunction("uname", liburl(a), Builtins.newTuple(self.BaseStr, self.BaseStr, self.BaseStr, self.BaseStr, self.BaseStr))

        def initProcMgmtBindings(self):
            """ generated source for method initProcMgmtBindings """
            a = "process-management"
            for s in Builtins.list_("EX_CANTCREAT", "EX_CONFIG", "EX_DATAERR", "EX_IOERR", "EX_NOHOST", "EX_NOINPUT", "EX_NOPERM", "EX_NOUSER", "EX_OK", "EX_OSERR", "EX_OSFILE", "EX_PROTOCOL", "EX_SOFTWARE", "EX_TEMPFAIL", "EX_UNAVAILABLE", "EX_USAGE", "P_NOWAIT", "P_NOWAITO", "P_WAIT", "P_DETACH", "P_OVERLAY", "WCONTINUED", "WCOREDUMP", "WEXITSTATUS", "WIFCONTINUED", "WIFEXITED", "WIFSIGNALED", "WIFSTOPPED", "WNOHANG", "WSTOPSIG", "WTERMSIG", "WUNTRACED"):
                addAttr(s, liburl(a), self.BaseNum)
            for s in Builtins.list_("abort", "execl", "execle", "execlp", "execlpe", "execv", "execve", "execvp", "execvpe", "_exit", "kill", "killpg", "plock", "startfile"):
                addFunction(s, liburl(a), self.None_)
            for s in Builtins.list_("nice", "spawnl", "spawnle", "spawnlp", "spawnlpe", "spawnv", "spawnve", "spawnvp", "spawnvpe", "system"):
                addFunction(s, liburl(a), self.BaseNum)
            addFunction("fork", liburl(a), self.newUnion(self.BaseFileInst, self.BaseNum))
            addFunction("times", liburl(a), Builtins.newTuple(self.BaseNum, self.BaseNum, self.BaseNum, self.BaseNum, self.BaseNum))
            for s in Builtins.list_("forkpty", "wait", "waitpid"):
                addFunction(s, liburl(a), Builtins.newTuple(self.BaseNum, self.BaseNum))
            for s in Builtins.list_("wait3", "wait4"):
                addFunction(s, liburl(a), Builtins.newTuple(self.BaseNum, self.BaseNum, self.BaseNum))

        def initFileBindings(self):
            """ generated source for method initFileBindings """
            a = "file-object-creation"
            for s in Builtins.list_("fdopen", "popen", "tmpfile"):
                addFunction(s, liburl(a), self.BaseFileInst)
            addFunction("popen2", liburl(a), Builtins.newTuple(self.BaseFileInst, self.BaseFileInst))
            addFunction("popen3", liburl(a), Builtins.newTuple(self.BaseFileInst, self.BaseFileInst, self.BaseFileInst))
            addFunction("popen4", liburl(a), Builtins.newTuple(self.BaseFileInst, self.BaseFileInst))
            a = "file-descriptor-operations"
            addFunction("open", liburl(a), self.BaseFileInst)
            for s in Builtins.list_("close", "closerange", "dup2", "fchmod", "fchown", "fdatasync", "fsync", "ftruncate", "lseek", "tcsetpgrp", "write"):
                addFunction(s, liburl(a), self.None_)
            for s in Builtins.list_("dup2", "fpathconf", "fstat", "fstatvfs", "isatty", "tcgetpgrp"):
                addFunction(s, liburl(a), self.BaseNum)
            for s in Builtins.list_("read", "ttyname"):
                addFunction(s, liburl(a), self.BaseStr)
            for s in Builtins.list_("openpty", "pipe", "fstat", "fstatvfs", "isatty"):
                addFunction(s, liburl(a), Builtins.newTuple(self.BaseNum, self.BaseNum))
            for s in Builtins.list_("O_APPEND", "O_CREAT", "O_DIRECT", "O_DIRECTORY", "O_DSYNC", "O_EXCL", "O_LARGEFILE", "O_NDELAY", "O_NOCTTY", "O_NOFOLLOW", "O_NONBLOCK", "O_RDONLY", "O_RDWR", "O_RSYNC", "O_SYNC", "O_TRUNC", "O_WRONLY", "SEEK_CUR", "SEEK_END", "SEEK_SET"):
                addAttr(s, liburl(a), self.BaseNum)

        def initFileAndDirBindings(self):
            """ generated source for method initFileAndDirBindings """
            a = "files-and-directories"
            for s in Builtins.list_("F_OK", "R_OK", "W_OK", "X_OK"):
                addAttr(s, liburl(a), self.BaseNum)
            for s in Builtins.list_("chflags", "chroot", "chmod", "chown", "lchflags", "lchmod", "lchown", "link", "mknod", "mkdir", "mkdirs", "remove", "removedirs", "rename", "renames", "rmdir", "symlink", "unlink", "utime"):
                addAttr(s, liburl(a), self.None_)
            for s in Builtins.list_("access", "lstat", "major", "minor", "makedev", "pathconf", "stat_float_times"):
                addFunction(s, liburl(a), self.BaseNum)
            for s in Builtins.list_("getcwdu", "readlink", "tempnam", "tmpnam"):
                addFunction(s, liburl(a), self.BaseStr)
            for s in Builtins.list_("listdir"):
                addFunction(s, liburl(a), Builtins.newList(self.BaseStr))
            addFunction("mkfifo", liburl(a), self.BaseFileInst)
            addFunction("stat", liburl(a), Builtins.newList(self.BaseNum))
            #  XXX: posix.stat_result
            addFunction("statvfs", liburl(a), Builtins.newList(self.BaseNum))
            #  XXX: pos.statvfs_result
            addAttr("pathconf_names", liburl(a), Builtins.newDict(self.BaseStr, self.BaseNum))
            addAttr("TMP_MAX", liburl(a), self.BaseNum)
            addFunction("walk", liburl(a), Builtins.newList(Builtins.newTuple(self.BaseStr, self.BaseStr, self.BaseStr)))

        def initMiscSystemInfo(self):
            """ generated source for method initMiscSystemInfo """
            a = "miscellaneous-system-information"
            addAttr("confstr_names", liburl(a), Builtins.newDict(self.BaseStr, self.BaseNum))
            addAttr("sysconf_names", liburl(a), Builtins.newDict(self.BaseStr, self.BaseNum))
            for s in Builtins.list_("curdir", "pardir", "sep", "altsep", "extsep", "pathsep", "defpath", "linesep", "devnull"):
                addAttr(s, liburl(a), self.BaseStr)
            for s in Builtins.list_("getloadavg", "sysconf"):
                addFunction(s, liburl(a), self.BaseNum)
            addFunction("confstr", liburl(a), self.BaseStr)

        def initOsPathModule(self):
            """ generated source for method initOsPathModule """
            m = Builtins.newModule("path")
            ospath = m.getTable()
            ospath.setPath("os.path")
            #  make sure global qnames are correct
            update("path", Builtins.newLibUrl("os.path.html#module-os.path"), m, MODULE)
            str_funcs = ["_resolve_link", "abspath", "basename", "commonprefix", "dirname", "expanduser", "expandvars", "join", "normcase", "normpath", "realpath", "relpath"]
            for s in str_funcs:
                ospath.insert(s, Builtins.newLibUrl("os.path", s), Builtins.newFunc(self.BaseStr), FUNCTION)
            num_funcs = ["exists", "lexists", "getatime", "getctime", "getmtime", "getsize", "isabs", "isdir", "isfile", "islink", "ismount", "samefile", "sameopenfile", "samestat", "supports_unicode_filenames"]
            for s in num_funcs:
                ospath.insert(s, Builtins.newLibUrl("os.path", s), Builtins.newFunc(self.BaseNum), FUNCTION)
            for s in Builtins.list_("split", "splitdrive", "splitext", "splitunc"):
                ospath.insert(s, Builtins.newLibUrl("os.path", s), Builtins.newFunc(Builtins.newTuple(self.BaseStr, self.BaseStr)), FUNCTION)
            ospath.insert("walk", Builtins.newLibUrl("os.path"), Builtins.newFunc(self.None_), FUNCTION)
            str_attrs = ["altsep", "curdir", "devnull", "defpath", "pardir", "pathsep", "sep"]
            for s in str_attrs:
                ospath.insert(s, Builtins.newLibUrl("os.path", s), self.BaseStr, ATTRIBUTE)
            ospath.insert("os", liburl(), self.module_, ATTRIBUTE)
            ospath.insert("stat", Builtins.newLibUrl("stat"), Builtins.newModule("<stat-fixme>"), ATTRIBUTE)
            #  XXX:  this is an re object, I think
            ospath.insert("_varprog", Builtins.newLibUrl("os.path"), Builtins.getUnknown(), ATTRIBUTE)

    class OperatorModule(NativeModule):
        """ generated source for class OperatorModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.OperatorModule, self).__init__("operator")

        def initBindings(self):
            """ generated source for method initBindings """
            #  XXX:  mark __getslice__, __setslice__ and __delslice__ as deprecated.
            addNumFuncs("__abs__", "__add__", "__and__", "__concat__", "__contains__", "__div__", "__doc__", "__eq__", "__floordiv__", "__ge__", "__getitem__", "__getslice__", "__gt__", "__iadd__", "__iand__", "__iconcat__", "__idiv__", "__ifloordiv__", "__ilshift__", "__imod__", "__imul__", "__index__", "__inv__", "__invert__", "__ior__", "__ipow__", "__irepeat__", "__irshift__", "__isub__", "__itruediv__", "__ixor__", "__le__", "__lshift__", "__lt__", "__mod__", "__mul__", "__name__", "__ne__", "__neg__", "__not__", "__or__", "__package__", "__pos__", "__pow__", "__repeat__", "__rshift__", "__setitem__", "__setslice__", "__sub__", "__truediv__", "__xor__", "abs", "add", "and_", "concat", "contains", "countOf", "div", "eq", "floordiv", "ge", "getitem", "getslice", "gt", "iadd", "iand", "iconcat", "idiv", "ifloordiv", "ilshift", "imod", "imul", "index", "indexOf", "inv", "invert", "ior", "ipow", "irepeat", "irshift", "isCallable", "isMappingType", "isNumberType", "isSequenceType", "is_", "is_not", "isub", "itruediv", "ixor", "le", "lshift", "lt", "mod", "mul", "ne", "neg", "not_", "or_", "pos", "pow", "repeat", "rshift", "sequenceIncludes", "setitem", "setslice", "sub", "truediv", "truth", "xor")
            addUnknownFuncs("attrgetter", "itemgetter", "methodcaller")
            addNoneFuncs("__delitem__", "__delslice__", "delitem", "delclice")

    class ParserModule(NativeModule):
        """ generated source for class ParserModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ParserModule, self).__init__("parser")

        def initBindings(self):
            """ generated source for method initBindings """
            st = Builtins.newClass("st", table, self.Object)
            st.getTable().insert("compile", Builtins.newLibUrl("parser", "st-objects"), Builtins.newFunc(), METHOD)
            st.getTable().insert("isexpr", Builtins.newLibUrl("parser", "st-objects"), Builtins.newFunc(self.BaseNum), METHOD)
            st.getTable().insert("issuite", Builtins.newLibUrl("parser", "st-objects"), Builtins.newFunc(self.BaseNum), METHOD)
            st.getTable().insert("tolist", Builtins.newLibUrl("parser", "st-objects"), Builtins.newFunc(Builtins.newList()), METHOD)
            st.getTable().insert("totuple", Builtins.newLibUrl("parser", "st-objects"), Builtins.newFunc(Builtins.newTuple()), METHOD)
            addAttr("STType", liburl("st-objects"), self.Type)
            for s in Builtins.list_("expr", "suite", "sequence2st", "tuple2st"):
                addFunction(s, liburl("creating-st-objects"), st)
            addFunction("st2list", liburl("converting-st-objects"), Builtins.newList())
            addFunction("st2tuple", liburl("converting-st-objects"), Builtins.newTuple())
            addFunction("compilest", liburl("converting-st-objects"), Builtins.getUnknown())
            addFunction("isexpr", liburl("queries-on-st-objects"), self.BaseBool)
            addFunction("issuite", liburl("queries-on-st-objects"), self.BaseBool)
            addClass("ParserError", liburl("exceptions-and-error-handling"), self.newException("ParserError", table))

    class PosixModule(NativeModule):
        """ generated source for class PosixModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.PosixModule, self).__init__("posix")

        def initBindings(self):
            """ generated source for method initBindings """
            addAttr("environ", liburl(), Builtins.newDict(self.BaseStr, self.BaseStr))

    class PwdModule(NativeModule):
        """ generated source for class PwdModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.PwdModule, self).__init__("pwd")

        def initBindings(self):
            """ generated source for method initBindings """
            struct_pwd = Builtins.newClass("struct_pwd", table, self.Object)
            for s in Builtins.list_("pw_nam", "pw_passwd", "pw_uid", "pw_gid", "pw_gecos", "pw_dir", "pw_shell"):
                struct_pwd.getTable().insert(s, liburl(), self.BaseNum, ATTRIBUTE)
            addAttr("struct_pwd", liburl(), struct_pwd)
            addFunction("getpwuid", liburl(), struct_pwd)
            addFunction("getpwnam", liburl(), struct_pwd)
            addFunction("getpwall", liburl(), Builtins.newList(struct_pwd))

    class PyexpatModule(NativeModule):
        """ generated source for class PyexpatModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.PyexpatModule, self).__init__("pyexpat")

        def initBindings(self):
            """ generated source for method initBindings """
            #  XXX

    class ReadlineModule(NativeModule):
        """ generated source for class ReadlineModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ReadlineModule, self).__init__("readline")

        def initBindings(self):
            """ generated source for method initBindings """
            addNoneFuncs("parse_and_bind", "insert_text", "read_init_file", "read_history_file", "write_history_file", "clear_history", "set_history_length", "remove_history_item", "replace_history_item", "redisplay", "set_startup_hook", "set_pre_input_hook", "set_completer", "set_completer_delims", "set_completion_display_matches_hook", "add_history")
            addNumFuncs("get_history_length", "get_current_history_length", "get_begidx", "get_endidx")
            addStrFuncs("get_line_buffer", "get_history_item")
            addUnknownFuncs("get_completion_type")
            addFunction("get_completer", liburl(), Builtins.newFunc())
            addFunction("get_completer_delims", liburl(), Builtins.newList(self.BaseStr))

    class ResourceModule(NativeModule):
        """ generated source for class ResourceModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ResourceModule, self).__init__("resource")

        def initBindings(self):
            """ generated source for method initBindings """
            addFunction("getrlimit", liburl(), Builtins.newTuple(self.BaseNum, self.BaseNum))
            addFunction("getrlimit", liburl(), Builtins.getUnknown())
            constants = ["RLIMIT_CORE", "RLIMIT_CPU", "RLIMIT_FSIZE", "RLIMIT_DATA", "RLIMIT_STACK", "RLIMIT_RSS", "RLIMIT_NPROC", "RLIMIT_NOFILE", "RLIMIT_OFILE", "RLIMIT_MEMLOCK", "RLIMIT_VMEM", "RLIMIT_AS"]
            for c in constants:
                addAttr(c, liburl("resource-limits"), self.BaseNum)
            ru = Builtins.newClass("struct_rusage", table, self.Object)
            ru_fields = ["ru_utime", "ru_stime", "ru_maxrss", "ru_ixrss", "ru_idrss", "ru_isrss", "ru_minflt", "ru_majflt", "ru_nswap", "ru_inblock", "ru_oublock", "ru_msgsnd", "ru_msgrcv", "ru_nsignals", "ru_nvcsw", "ru_nivcsw"]
            for ruf in ru_fields:
                ru.getTable().insert(ruf, liburl("resource-usage"), self.BaseNum, ATTRIBUTE)
            addFunction("getrusage", liburl("resource-usage"), ru)
            addFunction("getpagesize", liburl("resource-usage"), self.BaseNum)
            for s in Builtins.list_("RUSAGE_SELF", "RUSAGE_CHILDREN", "RUSAGE_BOTH"):
                addAttr(s, liburl("resource-usage"), self.BaseNum)

    class SelectModule(NativeModule):
        """ generated source for class SelectModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.SelectModule, self).__init__("select")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("error", liburl(), self.newException("error", table))
            addFunction("select", liburl(), Builtins.newTuple(Builtins.newList(), Builtins.newList(), Builtins.newList()))
            a = "edge-and-level-trigger-polling-epoll-objects"
            epoll = Builtins.newClass("epoll", table, self.Object)
            epoll.getTable().insert("close", Builtins.newLibUrl("select", a), Builtins.newFunc(self.None_), METHOD)
            epoll.getTable().insert("fileno", Builtins.newLibUrl("select", a), Builtins.newFunc(self.BaseNum), METHOD)
            epoll.getTable().insert("fromfd", Builtins.newLibUrl("select", a), Builtins.newFunc(epoll), METHOD)
            for s in Builtins.list_("register", "modify", "unregister", "poll"):
                epoll.getTable().insert(s, Builtins.newLibUrl("select", a), Builtins.newFunc(), METHOD)
            addClass("epoll", liburl(a), epoll)
            for s in Builtins.list_("EPOLLERR", "EPOLLET", "EPOLLHUP", "EPOLLIN", "EPOLLMSG", "EPOLLONESHOT", "EPOLLOUT", "EPOLLPRI", "EPOLLRDBAND", "EPOLLRDNORM", "EPOLLWRBAND", "EPOLLWRNORM"):
                addAttr(s, liburl(a), self.BaseNum)
            a = "polling-objects"
            poll = Builtins.newClass("poll", table, self.Object)
            poll.getTable().insert("register", Builtins.newLibUrl("select", a), Builtins.newFunc(), METHOD)
            poll.getTable().insert("modify", Builtins.newLibUrl("select", a), Builtins.newFunc(), METHOD)
            poll.getTable().insert("unregister", Builtins.newLibUrl("select", a), Builtins.newFunc(), METHOD)
            poll.getTable().insert("poll", Builtins.newLibUrl("select", a), Builtins.newFunc(Builtins.newList(Builtins.newTuple(self.BaseNum, self.BaseNum))), METHOD)
            addClass("poll", liburl(a), poll)
            for s in Builtins.list_("POLLERR", "POLLHUP", "POLLIN", "POLLMSG", "POLLNVAL", "POLLOUT", "POLLPRI", "POLLRDBAND", "POLLRDNORM", "POLLWRBAND", "POLLWRNORM"):
                addAttr(s, liburl(a), self.BaseNum)
            a = "kqueue-objects"
            kqueue = Builtins.newClass("kqueue", table, self.Object)
            kqueue.getTable().insert("close", Builtins.newLibUrl("select", a), Builtins.newFunc(self.None_), METHOD)
            kqueue.getTable().insert("fileno", Builtins.newLibUrl("select", a), Builtins.newFunc(self.BaseNum), METHOD)
            kqueue.getTable().insert("fromfd", Builtins.newLibUrl("select", a), Builtins.newFunc(kqueue), METHOD)
            kqueue.getTable().insert("control", Builtins.newLibUrl("select", a), Builtins.newFunc(Builtins.newList(Builtins.newTuple(self.BaseNum, self.BaseNum))), METHOD)
            addClass("kqueue", liburl(a), kqueue)
            a = "kevent-objects"
            kevent = Builtins.newClass("kevent", table, self.Object)
            for s in Builtins.list_("ident", "filter", "flags", "fflags", "data", "udata"):
                kevent.getTable().insert(s, Builtins.newLibUrl("select", a), Builtins.getUnknown(), ATTRIBUTE)
            addClass("kevent", liburl(a), kevent)

    class SignalModule(NativeModule):
        """ generated source for class SignalModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.SignalModule, self).__init__("signal")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumAttrs("NSIG", "SIGABRT", "SIGALRM", "SIGBUS", "SIGCHLD", "SIGCLD", "SIGCONT", "SIGFPE", "SIGHUP", "SIGILL", "SIGINT", "SIGIO", "SIGIOT", "SIGKILL", "SIGPIPE", "SIGPOLL", "SIGPROF", "SIGPWR", "SIGQUIT", "SIGRTMAX", "SIGRTMIN", "SIGSEGV", "SIGSTOP", "SIGSYS", "SIGTERM", "SIGTRAP", "SIGTSTP", "SIGTTIN", "SIGTTOU", "SIGURG", "SIGUSR1", "SIGUSR2", "SIGVTALRM", "SIGWINCH", "SIGXCPU", "SIGXFSZ", "SIG_DFL", "SIG_IGN")
            addUnknownFuncs("default_int_handler", "getsignal", "set_wakeup_fd", "signal")

    class ShaModule(NativeModule):
        """ generated source for class ShaModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ShaModule, self).__init__("sha")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumAttrs("blocksize", "digest_size")
            sha = Builtins.newClass("sha", table, self.Object)
            sha.getTable().insert("update", liburl(), Builtins.newFunc(), METHOD)
            sha.getTable().insert("digest", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            sha.getTable().insert("hexdigest", liburl(), Builtins.newFunc(self.BaseStr), METHOD)
            sha.getTable().insert("copy", liburl(), Builtins.newFunc(sha), METHOD)
            addClass("sha", liburl(), sha)
            update("new", liburl(), Builtins.newFunc(sha), CONSTRUCTOR)

    class SpwdModule(NativeModule):
        """ generated source for class SpwdModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.SpwdModule, self).__init__("spwd")

        def initBindings(self):
            """ generated source for method initBindings """
            struct_spwd = Builtins.newClass("struct_spwd", table, self.Object)
            for s in Builtins.list_("sp_nam", "sp_pwd", "sp_lstchg", "sp_min", "sp_max", "sp_warn", "sp_inact", "sp_expire", "sp_flag"):
                struct_spwd.getTable().insert(s, liburl(), self.BaseNum, ATTRIBUTE)
            addAttr("struct_spwd", liburl(), struct_spwd)
            addFunction("getspnam", liburl(), struct_spwd)
            addFunction("getspall", liburl(), Builtins.newList(struct_spwd))

    class StropModule(NativeModule):
        """ generated source for class StropModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.StropModule, self).__init__("strop")

        def initBindings(self):
            """ generated source for method initBindings """
            table.putAll(self.BaseStr.getTable())

    class StructModule(NativeModule):
        """ generated source for class StructModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.StructModule, self).__init__("struct")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("error", liburl(), self.newException("error", table))
            addStrFuncs("pack")
            addUnknownFuncs("pack_into")
            addNumFuncs("calcsize")
            addFunction("unpack", liburl(), Builtins.newTuple())
            addFunction("unpack_from", liburl(), Builtins.newTuple())
            self.BaseStruct = Builtins.newClass("Struct", table, self.Object)
            addClass("Struct", liburl("struct-objects"), self.BaseStruct)
            t = self.BaseStruct.getTable()
            t.insert("pack", liburl("struct-objects"), Builtins.newFunc(self.BaseStr), METHOD)
            t.insert("pack_into", liburl("struct-objects"), Builtins.newFunc(), METHOD)
            t.insert("unpack", liburl("struct-objects"), Builtins.newFunc(Builtins.newTuple()), METHOD)
            t.insert("unpack_from", liburl("struct-objects"), Builtins.newFunc(Builtins.newTuple()), METHOD)
            t.insert("format", liburl("struct-objects"), self.BaseStr, ATTRIBUTE)
            t.insert("size", liburl("struct-objects"), self.BaseNum, ATTRIBUTE)

    class SysModule(NativeModule):
        """ generated source for class SysModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.SysModule, self).__init__("sys")

        def initBindings(self):
            """ generated source for method initBindings """
            addUnknownFuncs("_clear_type_cache", "call_tracing", "callstats", "_current_frames", "_getframe", "displayhook", "dont_write_bytecode", "exitfunc", "exc_clear", "exc_info", "excepthook", "exit", "last_traceback", "last_type", "last_value", "modules", "path_hooks", "path_importer_cache", "getprofile", "gettrace", "setcheckinterval", "setprofile", "setrecursionlimit", "settrace")
            addAttr("exc_type", liburl(), self.None_)
            addUnknownAttrs("__stderr__", "__stdin__", "__stdout__", "stderr", "stdin", "stdout", "version_info")
            addNumAttrs("api_version", "hexversion", "winver", "maxint", "maxsize", "maxunicode", "py3kwarning", "dllhandle")
            addStrAttrs("platform", "byteorder", "copyright", "prefix", "version", "exec_prefix", "executable")
            addNumFuncs("getrecursionlimit", "getwindowsversion", "getrefcount", "getsizeof", "getcheckinterval")
            addStrFuncs("getdefaultencoding", "getfilesystemencoding")
            for s in Builtins.list_("argv", "builtin_module_names", "path", "meta_path", "subversion"):
                addAttr(s, liburl(), Builtins.newList(self.BaseStr))
            for s in Builtins.list_("flags", "warnoptions", "float_info"):
                addAttr(s, liburl(), Builtins.newDict(self.BaseStr, self.BaseNum))

    class SyslogModule(NativeModule):
        """ generated source for class SyslogModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.SyslogModule, self).__init__("syslog")

        def initBindings(self):
            """ generated source for method initBindings """
            addNoneFuncs("syslog", "openlog", "closelog", "setlogmask")
            addNumAttrs("LOG_ALERT", "LOG_AUTH", "LOG_CONS", "LOG_CRIT", "LOG_CRON", "LOG_DAEMON", "LOG_DEBUG", "LOG_EMERG", "LOG_ERR", "LOG_INFO", "LOG_KERN", "LOG_LOCAL0", "LOG_LOCAL1", "LOG_LOCAL2", "LOG_LOCAL3", "LOG_LOCAL4", "LOG_LOCAL5", "LOG_LOCAL6", "LOG_LOCAL7", "LOG_LPR", "LOG_MAIL", "LOG_MASK", "LOG_NDELAY", "LOG_NEWS", "LOG_NOTICE", "LOG_NOWAIT", "LOG_PERROR", "LOG_PID", "LOG_SYSLOG", "LOG_UPTO", "LOG_USER", "LOG_UUCP", "LOG_WARNING")

    class TermiosModule(NativeModule):
        """ generated source for class TermiosModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.TermiosModule, self).__init__("termios")

        def initBindings(self):
            """ generated source for method initBindings """
            addFunction("tcgetattr", liburl(), Builtins.newList())
            addUnknownFuncs("tcsetattr", "tcsendbreak", "tcdrain", "tcflush", "tcflow")

    class ThreadModule(NativeModule):
        """ generated source for class ThreadModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ThreadModule, self).__init__("thread")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("error", liburl(), self.newException("error", table))
            lock = Builtins.newClass("lock", table, self.Object)
            lock.getTable().insert("acquire", liburl(), self.BaseNum, METHOD)
            lock.getTable().insert("locked", liburl(), self.BaseNum, METHOD)
            lock.getTable().insert("release", liburl(), self.None_, METHOD)
            addAttr("LockType", liburl(), self.Type)
            addNoneFuncs("interrupt_main", "exit", "exit_thread")
            addNumFuncs("start_new", "start_new_thread", "get_ident", "stack_size")
            addFunction("allocate", liburl(), lock)
            addFunction("allocate_lock", liburl(), lock)
            #  synonym
            addAttr("_local", liburl(), self.Type)

    class TimeModule(NativeModule):
        """ generated source for class TimeModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.TimeModule, self).__init__("time")

        def initBindings(self):
            """ generated source for method initBindings """
            struct_time = self.Time_struct_time = InstanceType(Builtins.newClass("datetime", table, self.Object))
            addAttr("struct_time", liburl(), struct_time)
            struct_time_attrs = ["n_fields", "n_sequence_fields", "n_unnamed_fields", "tm_hour", "tm_isdst", "tm_mday", "tm_min", "tm_mon", "tm_wday", "tm_yday", "tm_year"]
            for s in struct_time_attrs:
                struct_time.getTable().insert(s, liburl("struct_time"), self.BaseNum, ATTRIBUTE)
            addNumAttrs("accept2dyear", "altzone", "daylight", "timezone")
            addAttr("tzname", liburl(), Builtins.newTuple(self.BaseStr, self.BaseStr))
            addNoneFuncs("sleep", "tzset")
            addNumFuncs("clock", "mktime", "time", "tzname")
            addStrFuncs("asctime", "ctime", "strftime")
            addFunctions_beCareful(struct_time, "gmtime", "localtime", "strptime")

    class UnicodedataModule(NativeModule):
        """ generated source for class UnicodedataModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.UnicodedataModule, self).__init__("unicodedata")

        def initBindings(self):
            """ generated source for method initBindings """
            addNumFuncs("decimal", "digit", "numeric", "combining", "east_asian_width", "mirrored")
            addStrFuncs("lookup", "name", "category", "bidirectional", "decomposition", "normalize")
            addNumAttrs("unidata_version")
            addUnknownAttrs("ucd_3_2_0")

    class ZipimportModule(NativeModule):
        """ generated source for class ZipimportModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ZipimportModule, self).__init__("zipimport")

        def initBindings(self):
            """ generated source for method initBindings """
            addClass("ZipImportError", liburl(), self.newException("ZipImportError", table))
            zipimporter = Builtins.newClass("zipimporter", table, self.Object)
            t = zipimporter.getTable()
            t.insert("find_module", liburl(), zipimporter, METHOD)
            t.insert("get_code", liburl(), Builtins.getUnknown(), METHOD)
            #  XXX:  code object
            t.insert("get_data", liburl(), Builtins.getUnknown(), METHOD)
            t.insert("get_source", liburl(), self.BaseStr, METHOD)
            t.insert("is_package", liburl(), self.BaseNum, METHOD)
            t.insert("load_module", liburl(), Builtins.newModule("<?>"), METHOD)
            t.insert("archive", liburl(), self.BaseStr, ATTRIBUTE)
            t.insert("prefix", liburl(), self.BaseStr, ATTRIBUTE)
            addClass("zipimporter", liburl(), zipimporter)
            addAttr("_zip_directory_cache", liburl(), Builtins.newDict(self.BaseStr, Builtins.getUnknown()))

    class ZlibModule(NativeModule):
        """ generated source for class ZlibModule """
        def __init__(self):
            """ generated source for method __init__ """
            super(Builtins.ZlibModule, self).__init__("zlib")

        def initBindings(self):
            """ generated source for method initBindings """
            Compress = Builtins.newClass("Compress", table, self.Object)
            for s in Builtins.list_("compress", "flush"):
                Compress.getTable().insert(s, Builtins.newLibUrl("zlib"), self.BaseStr, METHOD)
            Compress.getTable().insert("copy", Builtins.newLibUrl("zlib"), Compress, METHOD)
            addClass("Compress", liburl(), Compress)
            Decompress = Builtins.newClass("Decompress", table, self.Object)
            for s in Builtins.list_("unused_data", "unconsumed_tail"):
                Decompress.getTable().insert(s, Builtins.newLibUrl("zlib"), self.BaseStr, ATTRIBUTE)
            for s in Builtins.list_("decompress", "flush"):
                Decompress.getTable().insert(s, Builtins.newLibUrl("zlib"), self.BaseStr, METHOD)
            Decompress.getTable().insert("copy", Builtins.newLibUrl("zlib"), Decompress, METHOD)
            addClass("Decompress", liburl(), Decompress)
            addFunction("adler32", liburl(), self.BaseNum)
            addFunction("compress", liburl(), self.BaseStr)
            addFunction("compressobj", liburl(), Compress)
            addFunction("crc32", liburl(), self.BaseNum)
            addFunction("decompress", liburl(), self.BaseStr)
            addFunction("decompressobj", liburl(), Decompress)

