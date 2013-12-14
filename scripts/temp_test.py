
"""
simple testing script
"""

from pysonarsq.java.demos.Demo import Demo
import sys
import os
import fnmatch

def main():
    Demo.main(['./tests', './genned-html'])
    return
    
    matches = []
    for root, dirnames, filenames in os.walk('tests'):
        for filename in fnmatch.filter(filenames, '*.py'):
            matches.append(os.path.join(root, filename))

    for match in matches:
        if match in ('tests/ycomb.py'):
            Demo.main([match, os.path.join(*['genned-html'])])            

if __name__ == "__main__":
    sys.exit(main())
