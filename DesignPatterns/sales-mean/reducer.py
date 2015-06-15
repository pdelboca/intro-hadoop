#!/usr/bin/python
# Count: 345
# Nodes: [17583, 1007765, 1025821, 7004477, 9006895]
import csv
import sys
 
old_weekday = None
total_sales = 0

 
reader = csv.reader(sys.stdin, delimiter='\t')
 
for line in reader:
    
    weekday, sales = line

    if old_weekday and old_weekday != weekday:
        print "{0}\t{1}\t{2}".format(old_weekday, total_sales)
        total_sales = 0
        
 
    old_weekday = weekday
    total_sales += float(sales)
    
if old_weekday:
    print "{0}\t{1}".format(old_weekday, total_sales)
