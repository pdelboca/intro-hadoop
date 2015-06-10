#!/usr/bin/python
import sys

salesTotal = 0
salesCount = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data
    
    salesTotal += float(thisSale)
    salesCount += 1

print "Total", "\t", salesTotal, "\t", salesCount
