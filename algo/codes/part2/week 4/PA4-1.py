import os
from time import clock
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 4')

def load_data(fname):
    w=[]
    fhand=open(fname)
    for line in fhand:
        temp=line.split()
        if len(temp)==2:
            n=int(temp[0])
            w=[[float('inf') for i in range(n)] for j in range(n)]
            for i in range(n):
                w[i][i]=0
        if len(temp)>2:
            w[int(temp[0])-1][int(temp[1])-1]=int(temp[2])
    return n,w


def Floyd_Warshall(n,x):
    w=list(x)
    for k in range(n):
        if k%10==0:
            print k
        for i in range(n):
            for j in range(n):
                if w[i][k]+w[k][j]<w[i][j]:
                    w[i][j]=w[i][k]+w[k][j]
                if i==j and w[i][j]<0:
                    return 'NULL'

    for i in range(n):
        if w[i][i]<0:
            return 'NULL'
    re=min([min(i) for i in w])
    return re


if __name__ == '__main__':
    #fname='PA1test3.txt'
    fname='g3.txt'
    start=clock()
    n,w=load_data(fname)
    load_finish=clock()
    #print w
    print load_finish-start,'s for loading data'
    re=Floyd_Warshall(n,w)
    finish=clock()
    print re
    print finish-load_finish, 's for calculating'
