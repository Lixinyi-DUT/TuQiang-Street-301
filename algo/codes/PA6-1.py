import os
from time import clock
start=clock()
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def readint(fname):
    positives=dict()
    negatives=dict()
    fname=open(fname)
    for line in fname:
        temp=int(line)
        if temp>0:
            positives[temp]=0
        else:
            negatives[temp]=0
    return positives,negatives

def binsearch(x,a):
    l=len(a)
    if l==0:
        return 0
    if l==1:
        if a[0]>=x:
            return 0
        else:
            return 1
    mid=int(l/2)
    if a[mid]==x:
        return mid
    if a[mid]<x:
        return mid+1+binsearch(x,a[mid+1:])
    else:
        return binsearch(x,a[:mid])

fname='2SUM.txt'
p_values,n_values=readint(fname)
plength=len(p_values)
nlength=len(n_values)
p1=sorted(p_values.keys())
n1=sorted(n_values.keys())
sums=dict()
for i in range(10000):
    if i%100==0:
        print i
    x=n1[i]
    upper=10000-x
    lower=-10000-x
    start=binsearch(lower,p1)
    for j in range(start,plength):
        y=p1[j]
        if y>upper:
            break
        sums[x+y]=0
print len(sums)

for t in range(-10000,10000):
    if i%10==0:
        print i
    if t not in sums:
        for x in n_values:
            y=t-x
            if y!=x and y in p_values:
                sums[t]=0
                break

print len(sums)


# for t in range(-10000,10000):
#     for
# for i in range(l):
#     print i
#     x=values[i]
#     upper=10000-x
#     lower=-10000-x
#     if lower>values[-1]:
#         print i
#         continue
#     if upper<x:
#         break
#     start=binsearch(lower,values)
#     k=max(start,i+1)
#     for j in range(k,l):
#         y=values[j]
#         if y>upper:
#             break
#         sums[x+y]=sums.get(x+y,0)+1
# print len(sums)
# for t in range(-10000,10001):
#     for x in values:
#         y=t-x
#         if y!=x and y in values:
#             sums.append(t)
#             break
#     print t
# print len(sums)
# print sums
