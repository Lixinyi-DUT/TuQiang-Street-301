import os
import math
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def readadj(fname):
    adjlist=[]
    fhand=open(fname)
    for line in fhand:
        row=line.split()
        adj=[]
        for i in row[1:]:
            edge=i.split(',')
            adj.append((int(edge[0])-1,int(edge[1])))
        adjlist.append(adj)
    return adjlist

def init(v,s):
    X=[s]
    A=[math.inf for i in range(v)]
    A[s]=0
    B=[[] for i in range(v)]
    return X,A,B

def dijkstra(G,s,ver):
    X,A,B=init(ver,s)
    while len(X)<ver:
        obj=math.inf
        u2=-1
        for v in X:
            for (u,w) in G[v]:
                if u not in X:
                    if A[v]+w<obj:
                        obj=A[v]+w
                        u2=u
                        v2=v
                        w2=w
        if u2>0:
            X.append(u2)
            A[u2]=A[v2]+w2
            B[u2]=B[v2]+[u2]
    return A,B


g=readadj('dijkstraData.txt')
A,B=dijkstra(g,0,200)
p=[]
for i in [7,37,59,82,99,115,133,165,188,197]:
    p.append(A[i-1])

print(p)
