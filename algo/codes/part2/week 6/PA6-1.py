import os
from time import clock
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 6\')

t=[]
s=0

def load_data(fname):
    fhand=open(fname)
    n=0
    for line in fhand:
        temp=line.split()
        if len(temp)==1:
            n=int(temp[0])
            G=[[] for i in range(2*n+1)]
            Grev=[[] for i in range(2*n+1)]
        if len(temp)==2:
            v=int(temp[0])
            u=int(temp[1])
            G[n-v].append(n+u)
            G[n-u].append(n+v)
            Grev[n+u].append(n-v)
            Grev[n+v].append(n-u)
    return n,G,Grev

def DFS1(G,i):
    visited[i]=True
    for j in G[i]:
        if visited[j]==False:
            DFS1(G,j)
    t.append(i)

def DFS2(G,i):
    leader[i]=s
    for j in G[i]:
        if leader[j]<0:
            DFS2(G,j)

def Kosaraju_SCC(n,G,Grev):
    global t,s
    global visited
    global leader
    leader=[-1 for i in range(2*n+1)]
    visited=[False for i in range(2*n+1)]

    for i in range(2*n,-1,-1):
        if visited[i]==False:
            DFS1(Grev,i)
    t.reverse()
    #print t
    for i in t:
        if leader[i]<0:
            s=i
            DFS2(G,i)
    return leader

def find_self(n,G,Grev):
    leader=Kosaraju_SCC(n,G,Grev)
    #print leader
    for i in range(1,n+1):
        if leader[n-i]==leader[n+i]:
            return 0
    return 1

if __name__ == '__main__':
    re=[]
    for x in range(6):
        print '2SAT',x+1,'Start'
        fname='2sat'+str(x+1)+'.txt'
        #fname='PA1test1.txt'
        start=clock()
        n,G,Grev=load_data(fname)
        finish1=clock()
        print n,'variables'
        print finish1-start,'s for loading'
        r=find_self(n,G,Grev)
        re.append(r)
        finish2=clock()
        print r,'for data',x+1
        print finish2-finish1,'s for calculating'

    print re
