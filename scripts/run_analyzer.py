
from pysonarsq.java.demos.Demo import Demo
import sys

def main(_input, output):
    Demo.main([_input, output])

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:3]))