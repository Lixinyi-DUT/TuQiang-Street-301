import os
from time import clock
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 2')

def hamming_gen(string,k,c=-1):
    l=len(string)
    re=[]
    if k==0:
        return [string]
    if c==l:
        return []
    for i in range(l):
        if i>c:
            x=string[:i]+chr(ord('0')+ord('1')-ord(string[i]))+string[i+1:]
            re=re+hamming_gen(x,k-1,i)
            # if string[i]=='0':
            #     x=string[:i]+'1'+string[i+1:]
            #     re=re+hamming_gen(x,k-1,i)
    return re

def load_data(fname):
    table=dict()
    fhand=open(fname)
    label=0
    for line in fhand:
        t=line.split()
        if len(t)==2:
            n,b=int(t[0]),int(t[1])
            leader=[i for i in range(n)]
        if len(t)==b:
            s=''.join([i for i in t])
            if s in table:
                leader[label]=table[s]
            else:
                table[s]=label
            label=label+1
    return table,leader,n,b

def leader_update(leader,n,a,b): # merge the leaders by the leader with larger size of cluster
    if leader.count(a)<leader.count(b):
        for i in range(n):
            if leader[i]==a:
                leader[i]=b
    else:
        for i in range(n):
            if leader[i]==b:
                leader[i]=a
    return leader

def find_cluster(leader,table,n):
    for k in range(1,3):
        t=0
        for i in table:
            dist=hamming_gen(i,k)
            label=table[i]
            for j in dist:
                if j in table and j>i:
                    p=table[j]
                    if leader[label]!=leader[p]:
                        leader=leader_update(leader,n,leader[label],leader[p])
            t=t+1
            if t%1000==0:
                print t
    #print leader
    print len(set(leader))


if __name__ == '__main__':
    fname='clustering_big.txt'
    #fname='PA2test1.txt'
    start=clock()
    t,l,n,b=load_data(fname)
    load_finish=clock()
    print load_finish-start,'s for loading data'
    find_cluster(l,t,n)
    find_finish=clock()
    print find_finish-load_finish, 's for calculating'
    print hamming_gen('010100',2)
