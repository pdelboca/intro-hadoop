#!/usr/bin/python
#import sys
# 
#current_word = None
#current_count = 1
#node_list = []
# 
#for line in sys.stdin:
#    
#    word, count, node = line.strip().split('\t')
#
#    if current_word:
#        if word == current_word:
#            current_count += int(count)
#            if node not in node_list:            
#                node_list.append(node)
#        else:
#            print "{0}\t{1}\t{2}".format(current_word, current_count, node_list)
#            current_count = 1
#            node_list = []
# 
#    current_word = word
#    if node not in node_list:            
#        node_list.append(node)
# 
#if current_count > 1:
#    print "{0}\t{1}\t{2}".format(current_word, current_count, node_list)

import sys
def reducer():
    oldKey = None
    array = []
    for line in sys.stdin:
        data = line.strip().split("\t");
        thisKey, word = data;
        if oldKey and oldKey != thisKey:
                print oldKey,'\t','\t'.join(array)
                array=[]
        oldKey=thisKey
        array.append(word)
    if oldKey:
        print oldKey,'\t','\t'.join(array)
def main():
    import StringIO
    reducer()

if __name__ == "__main__":
    main()