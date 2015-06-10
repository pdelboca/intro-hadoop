#!/usr/bin/python
import sys
old_url = None
hit_count = 0


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    url, hit = data
    if old_url and old_url != url:
        print old_url, "\t", hit_count
        old_url = url
        hit_count = 0

    old_url = url
    hit_count += +1

if old_url != None:
    print old_url, "\t", hit_count