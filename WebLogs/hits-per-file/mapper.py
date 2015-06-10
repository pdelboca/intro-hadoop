#!/usr/bin/python
import sys
import re

p = re.compile(
    '^(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+]) "(\S+) (.*?) (\S+)" (\S+) (\S+)'
    )
    
    
for line in sys.stdin:
    m = p.match(line)
    
    if not m:
        continue

    client, identuser, authuser, date, time, tz, method, url, protocol, status, num_bytes = m.groups()
    print "{0}\t{1}".format(url, 1)
    