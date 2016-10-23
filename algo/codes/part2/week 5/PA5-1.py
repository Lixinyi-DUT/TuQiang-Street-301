import os
from time import clock
import numpy as np
import itertools
from itertools import chain, combinations
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 5')

def load_data(fname):
    pos=[]
    fhand=open(fname)
    for line in fhand:
        temp=line.split()
        if len(temp)==1:
            n=int(temp[0])
        if len(temp)==2:
            pos.append((float(temp[0]),float(temp[1])))
    return n,pos

def dist(a,b): #return Euclidean distance between two locations (tuple)
    pos1=np.array(a)
    pos2=np.array(b)
    return np.linalg.norm(pos1-pos2)


def dp_tsp(n,pos):
    A=dict()
    p=list(set(chain.from_iterable(combinations(range(n),i) for i in range(n+1))))
    print len(p)
    for x in p:
        s=sorted(list(x))
        A[tuple(s)]=[float('inf') for i in range(n)]
        if s==[0]:
            A[tuple(s)][0]=0
    for m in range(1,n):
        cand_set=list(combinations(range(1,n), m))
        for x in cand_set:
            s=sorted(list(x))
            for j in s:
                temp=[0]+s
                temp.remove(j)
                A[tuple([0]+s)][j]=min([(A[tuple(temp)][k]+dist(pos[k],pos[j])) for k in temp])
        print m

    return min([(A[tuple(range(n))][j]+dist(pos[j],pos[0])) for j in range(1,n)])

def set2index(n,s):
    t=['0' for i in range(n)]
    for i in range(n):
        if i in s:
            t[n-1-i]='1'
    num=''.join(t)
    return int(num,2)

def is_inset(i,s,n):
    num=bin(s)[2:].zfill(n)
    return num[n-1-i]=='1'

def insert2set(i,s,n):
    num=bin(s)[2:].zfill(n)
    x=num[:n-1-i]+'1'+num[n-i:]
    return int(x,2)

def delfromset(i,s,n):
    num=bin(s)[2:].zfill(n)
    x=num[:n-1-i]+'0'+num[n-i:]
    return int(x,2)

def num2set(s,n):
    l=[]
    num=bin(s)[2:].zfill(n)
    for i in range(n):
        if num[i]=='1':
            l.append(n-1-i)
    return l

def dp_tsp_v2(n,pos):
    d=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j]=dist(pos[i],pos[j])
    A=dict()
    A[1]=dict()
    A[1][0]=0
    for m in range(1,n):
        B=dict()
        for x in A:
            x_set=num2set(x,n)
            for y in set(range(1,n))-set(x_set):
                s=insert2set(y,x,n)
                if s not in B:
                    B[s]=dict()
                    B[s][0]=float('inf')
                    #print num2set(x,n)
                B[s][y]=min([(A[x][k]+d[k][y]) for k in x_set])
        print 'm=',m
        A=B
    return min([(A[2**n-1][j]+d[j][0]) for j in range(1,n)])





if __name__ == '__main__':
    fname='tsp.txt'
    #fname='PA1test2.txt'
    start=clock()
    n,pos=load_data(fname)
    load_finish=clock()
    print load_finish-start, 's for loading'
    #print range(1,n)
    re=dp_tsp_v2(n,pos)
    # for i in set(set(range(5))-set([1,2])):
    #     print i
    cal_finish=clock()
    print re
    print cal_finish-load_finish,'s for calculating'
