"""
some tools for helping convert in bulk
"""

import fnmatch
import os
import subprocess

matches = []
for root, dirnames, filenames in os.walk('.'):
  for filename in fnmatch.filter(filenames, '*.java'):
      name = filename.split('.', 1)[0]
      py_equiv = os.path.join(root, name + '.py')
      if not os.path.exists(py_equiv):
          matches.append(os.path.join(root, filename))
      
for file in matches:
    name = file.rsplit('.', 1)[0] + '.py'
    
    print('=' * 80)
    print('\tconverting %s to %s' % (file, name))
    print('=' * 80)    
    
    subprocess.call(['j2py', file, name])
    
# getting working mostly involved replacing <> with e.g. <String>, except in one case
# where needed to do a test for expr.children.remove(item), that item was contained
# then
# find ./* -name *.java | xargs rm -f
#
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.jetbrains\.annotations\.NotNull/from org.jetbrains.annotations import NotNull/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.jetbrains\.annotations\.Nullable/from org.jetbrains.annotations import Nullable/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.jetbrains\.annotations\.Nullable/from org.jetbrains.annotations import Nullable/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.yinwang\.pysonar\.types.\([a-zA-Z]*\)/from pysonarsq.java.types.\1 import \1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.yinwang\.pysonar\.\([a-zA-Z]*\)/from pysonarsq.java.\1 import \1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import org\.yinwang\.pysonar\.ast/from pysonarsq.java.ast import */g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import java\.util\.\([a-zA-Z]*\)/from java.util import \1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/import java\.io\.\([a-zA-Z]*\)/from java.io import \1/g'

# java2python failures
# find ./* -name \*.py | xargs sed -i '' -e 's/def equals\(\.*\)/def __eq__\1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/isinstance(self,/isinstance(self,/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/StringBuilder()/[]/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/sb\.__str__()/"".join\(sb\)/g'


# misc:
# find ./* -name \*.py | xargs sed -i '' -e 's/from pysonarsq\.java\.ast import *.*/from pysonarsq.java.ast import */g'
# find ./* -name \*.py | xargs sed -i '' -e 's/from pysonarsq\.java\. import _/from pysonarsq.java._ import _/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/\(from java.util import Map.Entry\)/#\1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/\(@overloaded\)/#\1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/\(@.*\.register\)/#\1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/\(@.*\.register\)/#\1/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/\(addChildren\)/self.\1/g'

# find ./* -name \*.py | xargs sed -i '' -e 's/\.entrySet(/.items(/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/startsWith/startswith/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/    visitNode/    self.visitNode/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/sb\.__str__()/''.join(sb)/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/ == None/ is None/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/ != None/ is not None/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/__init__(start, end)/__init__(start, end)/g'
# find ./* -name \*.py | xargs sed -i '' -e 's/    self.resolveExpr/    self.resolveExpr/g'

# --- no! ---- find ./* -name \*.py | xargs sed -i '' -e 's/\.add(/.append(/g'

# java.util.Logging.Level...
# java.util.Map.Entry
# java.util.regex.Pattern
# java.util.SortedSet, TreeSet
