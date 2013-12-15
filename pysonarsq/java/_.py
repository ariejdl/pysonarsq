#!/usr/bin/env python
""" generated source for module _ """
# package: org.yinwang.pysonar
from org.jetbrains.annotations import NotNull

from org.jetbrains.annotations import Nullable

from java.io import File

#import java.lang.management.GarbageCollectorMXBean

#import java.lang.management.ManagementFactory

#import java.nio.charset.Charset

#import java.security.MessageDigest

#import java.text.DecimalFormat

import java.util

# === py

import hashlib
import tempfile
import os
import uuid
import time
import re

# 
#  * unsorted utility class
#  
class _(object):
    #UTF_8 = Charset.forName("UTF-8")

    @classmethod    
    def parentFile(cls, fileOrDir):
        return os.path.abspath(os.path.join(fileOrDir, os.pardir))
    
    @classmethod
    def millis(cls):
        return int(round(time.time() * 1000))
    
    @classmethod
    def isEmpty(cls, _dict):
        if isinstance(_dict, set):
            return len(_dict) == 0
            
        elif isinstance(_dict, dict):
            for k in _dict.iterkeys():
                return False
        
        return len(_dict) == 0

    @classmethod
    def baseFileName(cls, filename):
        return File(filename).__name__

    @classmethod
    def getSystemTempDir(cls):
        return tempfile.gettempdir() + os.sep

    # 
    #      * Returns the parent qname of {@code qname} -- everything up to the
    #      * last dot (exclusive), or if there are no dots, the empty string.
    #      
    @classmethod
    def getQnameParent(cls, qname):
        if qname is None or qname.isEmpty():
            return ""
        index = qname.lastIndexOf(".")
        if index == -1:
            return ""
        return qname[0:index]

    @classmethod
    def moduleQname(cls, file_):
        if file_.endswith("__init__.py"):
            file_ = os.path.join(*file_.split(os.sep)[:-1])
        elif file_.endswith(".py"):
            file_ = file_[0 : (len(file_) - len(".py"))]
            
        return file_.replace(".", "%20").replace('/', '.').replace('\\', '.')

    @classmethod
    def moduleName(cls, path):
        path = os.path.abspath(path)         
        name = path.rsplit(os.sep)[-1]
        
        if name == "__init__.py":
            return path.rsplit(os.sep)[-2]
        elif name.endswith(".py"):
            return name.replace('.py', '')
        else:
            return name

    @classmethod
    def arrayToString(cls, strings):
        sb = StringBuffer()
        for s in strings:
            sb.append(s).append("\n")
        return "".join(sb)

    @classmethod
    def arrayToSortedStringSet(cls, strings):
        raise Exception('not tested')
        sorter = TreeSet()
        sorter.addAll(strings)
        return cls.arrayToString(sorter)

    @classmethod
    def writeFile(cls, path, contents):
        if not os.path.exists(_.parentFile(path)):
            os.mkdir(_.parentFile(path))
        with open(path, 'wb') as f:
            f.write(contents.encode('utf-8'))

    @classmethod
    #@overloaded
    def readFile(cls, filename):
        """ generated source for method readFile """
        with open(filename, 'r') as f:
            return f.read()

    @classmethod
    def getBytesFromFile(cls, file_):
        if isinstance(file_, file):
            return file_.read()
        with open(file_, 'rb') as f:
            return f.read()

    @classmethod
    def isReadableFile(cls, path):
        """ generated source for method isReadableFile """
        return os.path.isfile(path)

    @classmethod
    def readWhole(cls, is_):
        return is_.read()

    @classmethod
    def getSHA1(cls, path):
        """ generated source for method getSHA1 """
        bytes = cls.getBytesFromFile(path)
        return cls.getMD5(bytes)

    @classmethod
    def getMD5(cls, fileContents):
        return hashlib.md5(fileContents).hexdigest()

    @classmethod
    def escapeQname(cls, s):
        """ generated source for method escapeQname """
        #return s.replaceAll("[.&@%-]", "_")
        return re.sub("[.&@%-]", '_', s)

    @classmethod
    def escapeWindowsPath(cls, path):
        """ generated source for method escapeWindowsPath """
        return path.replace("\\", "\\\\")

    @classmethod
    def __str__Collection(cls, collection):
        """ generated source for method toStringCollection """
        ret = ArrayList()
        for x in collection:
            ret.add(str(x))
        return ret

    @classmethod
    def joinWithSep(cls, ls, sep, start, end):
        return start + sep.join(ls) + end

    @classmethod
    def msg(cls, m):
        print('log:' + m)

    @classmethod
    #@die.register(object, str, Exception)
    def die(cls, msg=None, e=None):

        if msg is not None:
            print('Exception: ' + msg)
        if e is not None:
            print("Exception: " + e + "\n")

        import traceback, sys            
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

        sys.exit(1)

    @classmethod
    def readWholeFile(cls, filename):
        """ generated source for method readWholeFile """
        try:
            return Scanner(File(filename)).useDelimiter("PYSONAR2END").next()
        except FileNotFoundException as e:
            return None

    @classmethod
    def readWholeStream(cls, in_):
        """ generated source for method readWholeStream """
        return Scanner(in_).useDelimiter("\\Z").next()

    @classmethod
    def percent(cls, num, total):
        """ generated source for method percent """
        if total == 0:
            return "100%"
        else:
            return "{0:.2f}".format(100 * num / (total * 1.0)) + '%'

    @classmethod
    def formatTime(cls, millis):
        """ generated source for method formatTime """
        sec = millis / 1000
        min = sec / 60
        sec = sec % 60
        hr = min / 60
        min = min % 60
        return "%02d:%02d:%02d" % (hr,min,sec)

    @classmethod
    def formatNumber(cls, n, length):
        if length == 0:
            length = 1
            
        if isinstance(n, (int, )):
            return ('%0' + str(length) + 'd') % int(n)
        elif isinstance(n, (long, )):
            return ('%0' + str(length) + 'd') % long(n)
        else:
            return ('%0' + str(length) + 's') % long(n)            

    @classmethod
    def deleteDirectory(cls, directory):

        if directory.exists():
            if files is not None:
                for f in files:
                    if f.isDirectory():
                        cls.deleteDirectory(f)
                    else:
                        f.delete()
        return directory.delete()

    @classmethod
    def newSessionId(cls):
        """ generated source for method newSessionId """
        return str(uuid.uuid4())

    @classmethod
    def makePath(cls, *files):
        ret = File(files[0])
        i = 1
        while len(files):
            ret = File(ret, files[i])
            i += 1
        return ret

    @classmethod
    def makePathString(cls, *frags):
        return os.path.join(*frags)

    @classmethod
    def unifyPath(cls, filename):
        if isinstance(filename, file):
            return os.path.abspath(filename.name)
        return os.path.abspath(filename)

    @classmethod
    def relPath(cls, path1, path2):
        return os.path.relpath(path1, path2)

    @classmethod
    def joinPath(cls, dir, file_):
        """ generated source for method joinPath """
        return os.sep.join([os.path.abspath(dir), file_])

    @classmethod
    def banner(cls, msg):
        """ generated source for method banner """
        return "---------------- " + msg + " ----------------"

    @classmethod
    def printMem(cls, bytes):
        """ generated source for method printMem """
        dbytes = float(bytes)
        df = "{0:.2f}"
        if dbytes < 1024:
            return df.format(bytes)
        elif dbytes < 1024 * 1024:
            return df.format(dbytes / 1024)
        elif dbytes < 1024 * 1024 * 1024:
            return df.format(dbytes / 1024 / 1024) + "M"
        elif dbytes < 1024 * 1024 * 1024 * 1024L:
            return df.format(dbytes / 1024 / 1024 / 1024) + "G"
        else:
            return "Too big to show you"

    @classmethod
    def getGCStats(cls):
        # left as an exercise to the reader
        """ 
        totalGC = 0
        gcTime = 0
        for gc in ManagementFactory.getGarbageCollectorMXBeans():
            if count >= 0:
                totalGC += count
            if time >= 0:
                gcTime += time
        sb = []
        sb.append(cls.banner("memory stats"))
        sb.append("\n- total collections: " + totalGC)
        sb.append("\n- total collection time: " + cls.formatTime(gcTime))
        runtime = Runtime.getRuntime()
        sb.append("\n- total memory: " + _.printMem(runtime.totalMemory()))
        return "".join(sb)
        """
        return '-- gc stats go here -- =) '

