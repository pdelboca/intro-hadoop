#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if len(line) != 6:
        continue
    
    date, hour, shop, category, amount, method = line
    weekday = datetime.strptime(date, "%Y-%m-%d").weekday()        
    
    print '{0}\t{1}'.format(weekday, amount)