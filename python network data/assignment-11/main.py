'''Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.'''

import re
import os
os.chdir(r'F:\TuQiang-Street-301\python network data\assignment-11')

#Clear Structure of Code:
#data=open('regex_sum_42.txt')
data=open('regex_sum_294690.txt')
numlist=[]
for line in data:
    temp=re.findall('[0-9]+',line)
    numlist=numlist+temp

print len(numlist)

s=0
for num in numlist:
    s=s+int(num)

print s

#One line Version:
print sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_294690.txt').read())])
