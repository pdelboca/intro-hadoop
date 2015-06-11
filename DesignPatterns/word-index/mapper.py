#!/usr/bin/python
import sys
import csv
header_line = True

reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)  

for line in reader:

    if header_line:
        header_line = False
        continue
    
    node = line[0]
    body = line[4].lower()    
    characters = '.,!?:;"()<>[]#$=-/'
    for c in characters:
        body = body.replace(c,' ')
    
    words = body.strip().split()
    
    for word in words:
        print '{0}\t{1}\t{2}'.format(word,1,node)