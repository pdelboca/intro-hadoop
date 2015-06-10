#!/usr/bin/python
import sys

max_sale = 0
old_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    this_key, this_sale = data

    # Detect categories changed so print
    if old_key and this_key != old_key:
        print old_key, "\t", max_sale
        old_key = this_key
        max_sale = 0
    
    if max_sale == 0 or max_sale < this_sale:
        old_key = this_key
        max_sale = this_sale

# The last category will never enter the if condition
if old_key != None:
    print old_key, "\t", max_sale