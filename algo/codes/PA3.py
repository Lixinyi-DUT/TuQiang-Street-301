import os
import random
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def readpa3data(fname):
    fhand=open(fname)
    edges=[]
    for line in fhand:
        temp=line.split()
        for i in temp[1:]:
            if int(temp[0])<int(i):
                t=(int(temp[0]),int(i))
                edges.append(t)
    return edges

def karger(edges,verticles):
    e=list(edges)
    ver=list(verticles)
    while len(ver)>2:
        k=random.randint(0,len(e)-1)
        (v,u)=e[k]
        e.remove(e[k])
        for i in range(len(e)):
            temp=e[i]
            if temp[0]==u:
                e[i]=(v,temp[1])
            if temp[1]==u:
                e[i]=(temp[0],v)
        while (v,v) in e:
            e.remove((v,v))
        ver.remove(u)
    return e

def minicut(edges,verticles):
    result=list()
    for i in range(100):
        x=len(karger(edges,verticles))
        print x
        result.append(x)
    return min(result)


# t1=readpa3data('PA3test1.txt')
# t2=readpa3data('PA3test2.txt')
# t3=readpa3data('PA3test3.txt')
# t4=readpa3data('PA3test4.txt')
test=readpa3data('KargerMinCut.txt')
#print test
#print len(test)
# print karger(t1,a)
# print karger(t1,range(1,9))
#print karger(t2,range(1,9))
#print karger(t3,range(1,201))
print minicut(test,range(1,201))
