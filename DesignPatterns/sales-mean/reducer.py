#!/usr/bin/python
# Count: 345
# Nodes: [17583, 1007765, 1025821, 7004477, 9006895]
import csv
import sys
 
old_weekday = None
total_sales = 0
day_counts = 0

 
reader = csv.reader(sys.stdin, delimiter='\t')
 
for line in reader:
    
    weekday, sales = line

    if old_weekday and old_weekday != weekday:
        print "{0}\t{1}".format(old_weekday, total_sales/day_counts)
        day_counts = 0
        total_sales = 0
        
 
    old_weekday = weekday
    day_counts += 1
    total_sales += float(sales)
    
if old_weekday:
    print "{0}\t{1}".format(old_weekday, total_sales)
