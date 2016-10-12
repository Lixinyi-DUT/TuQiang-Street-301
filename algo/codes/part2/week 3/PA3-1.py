import os
from time import clock
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 3')

def load_data(fname):
    v=[]
    w=[]
    size=0
    n=0
    fhand=open(fname)
    head=True
    for line in fhand:
        temp=line.split()
        if len(temp)>1:
            if head:
                size=int(temp[0])
                n=int(temp[1])
                head=False
            else:
                v.append(int(temp[0]))
                w.append(int(temp[1]))
    return size,n,v,w

def knapsack(size,n,v,w):
    A=[[0 for i in range(size+1)] for i in range(n+1)]
    # for i in range(size+1):
    #     A[0][i]=0
    for i in range(1,n+1):
        for x in range(size+1):
            if x-w[i-1]<0:
                A[i][x]=A[i-1][x]
            else:
                A[i][x]=max(A[i-1][x],A[i-1][x-w[i-1]]+v[i-1])
    return A[n][size]

if __name__ == '__main__':
    fname='knapsack1.txt'
    #fname='PA1test2.txt'
    start=clock()
    size,n,v,w=load_data(fname)
    load_finish=clock()
    print load_finish-start, 's for loading data'
    result=knapsack(size,n,v,w)
    print result
    finish=clock()
    print finish-load_finish,'s for computing'
