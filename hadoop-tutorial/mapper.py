#!/usr/bin/python

import sys


# read standard input line by line
for line in sys.stdin:
    # strip off extra whitespace, split on tab and put the data in an array
    data = line.strip().split("\t")

    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
