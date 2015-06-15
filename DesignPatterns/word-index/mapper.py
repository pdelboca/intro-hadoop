#!/usr/bin/python
#import sys
#import csv
#header_line = True
#
#reader = csv.reader(sys.stdin, delimiter='\t')
##writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)  
#
#for line in reader:
#
#    if header_line:
#        header_line = False
#        continue
#
#    if line[8]=="added_at":
#        continue;
#    
#    node = line[0]
#    body = line[4].lower()    
#    characters = '.,!?:;"()<>[]#$=-/'
#    for c in characters:
#        body = body.replace(c,' ')
#    
#    words = body.strip().split()
#    
#    for word in words:
#        print '{0}\t{1}\t{2}'.format(word,1,node)

import sys
import csv
import re
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    delimiters = ['[',']','#','$','-','=','/',' ','\t','\n','.','!','?',':',';','\"','(',')','<','>',','];
    regexPattern = '|'.join(map(re.escape, delimiters))
    for line in reader:
        #skip header..
        if line[8]=="added_at":
             continue;
        node = line[0];
        body = line[4];
        words = re.split(regexPattern, body.lower(), 0)
        for word in words:
                if len(word)>0:
                        print word, '\t', node;
def main():
    import StringIO
    mapper()

if __name__ == "__main__":
    main()