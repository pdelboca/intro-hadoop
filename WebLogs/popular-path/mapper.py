#!/usr/bin/python
import sys
import re
import operator

log_reg = re.compile(
    '^(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+]) "(\S+) (.*?) (\S+)" (\S+) (\S+)'
    )
path_reg = re.compile('(\/.*)$')

d = {}

for line in sys.stdin:
    m = log_reg.match(line)
    
    if not m:
        continue

    client, identuser, authuser, date, time, tz, method, url, protocol, status, num_bytes = m.groups()
    path = path_reg.findall(url)[0]
    
    if path in d:
      d[path] += 1
    else:
      d[path] = 1

popular_path = max(d.iteritems(), key=operator.itemgetter(1))

print "{0}\t{1}".format(popular_path[0], popular_path[1])
