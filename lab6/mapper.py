import sys

for line in sys.stdin:
    keys = line.strip().split()
    for key in keys:
        print( "%s\t%d" % (key, 1) )
