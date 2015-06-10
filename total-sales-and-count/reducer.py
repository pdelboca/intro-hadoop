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
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal, "\t", salesCount
        oldKey = thisKey
        salesTotal = 0
        salesCount = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    salesCount += 1

if oldKey != None:
    print oldKey, "\t", salesTotal, "\t", salesCount
