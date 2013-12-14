
import sys
import types

import functools

#
# JETBRAINS
#

org = types.ModuleType('org', 'org module')
jetbrains = types.ModuleType('jetbrains', 'jetbrains module')
annotations = types.ModuleType('annotations', 'jetbrains module')

if 'setup jetbrains':
    def NotNull(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            print 'Calling decorated function'
            return f(*args, **kwds)
        return wrapper

    def Nullable(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            print 'Calling decorated function'
            return f(*args, **kwds)
        return wrapper        
    
    annotations.NotNull = NotNull
    annotations.Nullable = Nullable
            
org.jetbrains = jetbrains
org.jetbrains.annotations = annotations

sys.modules['org'] = org
sys.modules['org.jetbrains'] = jetbrains
sys.modules['org.jetbrains.annotations'] = annotations

#
# JAVA
#

java = types.ModuleType('java', 'java module')
util = types.ModuleType('util', 'util module')
io = types.ModuleType('io', 'io module')
fake = types.ModuleType('fake', 'fake module')

class Url(str):
    def __init__(self, _str):
        self = _str

if 'setup java':
    from collections import OrderedDict
    from orderedset import OrderedSet

    util.ArrayList = list
    util.List = list
    util.HashMap = dict
    util.HashSet = set
    util.Map = dict
    util.Set = set
    util.LinkedHashMap = OrderedDict
    
    util.TreeSet = OrderedSet
    util.SortedSet = OrderedSet    
    
    io.File = file

    #fake.Url = Url # no!

    
sys.modules['java'] = java
sys.modules['java.util'] = util
sys.modules['java.io'] = io
sys.modules['java.fake'] = fake

