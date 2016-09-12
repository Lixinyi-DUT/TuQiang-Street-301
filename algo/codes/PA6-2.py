                i
                mport os
import heapq
from time import clock
start=clock()
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def readdata(fname):
    a=list()
    fhand=open(fname)
    for line in fhand:
        a.append(int(line))
    return a
load_time=

def maintainmedian(stream):
    medians=[]
    for i in range(len(stream)):
        a=sorted(stream[:i+1])
        m=a[int(i/2)]
        medians.append(m)
    return medians

fname='Median.txt'
data=readdata(fname)
lst=maintainmedian(data)
final1=clock()
print sum(lst)%10000,'use ',final1-start,'s'
