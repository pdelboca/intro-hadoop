#!/usr/bin/python
import sys
import operator

d = {}
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    path, hit = data

    if path in d:
      d[path] += 1
    else:
      d[path] = 1

popular_path = max(d.iteritems(), key=operator.itemgetter(1))

print "{0}\t{1}".format(popular_path[0], popular_path[1])
