#!/usr/bin/python
import sys
 
old_word = None
current_count = 0
node_list = []
 
for line in sys.stdin:
    
    word, count, node = line.strip().split('\t')

    if old_word and old_word != word:
       print "{0}\t{1}\t{2}".format(old_word, current_count, node_list)
       current_count = 0
       node_list = []
 
    old_word = word
    current_count += 1
    if node not in node_list:            
        node_list.append(node)
 
if old_word:
    print "{0}\t{1}\t{2}".format(old_word, current_count, node_list)
