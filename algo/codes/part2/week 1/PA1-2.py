import os
from time import clock
from heapq import heappush, heappop, heapify
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 1')


def Load_data(fname):
    fhand=open(fname)
    for lines in fhand:
        info=lines.split()
        if len(info) == 2:
            n=int(info[0])
            G=[[] for i in range(n)]
        if len(info)>2:
            v=int(info[0])-1 #for the sake of space, value of v means the vertice v+1, so is u
            u=int(info[1])-1
            w=int(info[2])
            G[v].append((u,w))
            G[u].append((v,w))
    return G

def Naive_Prim_MST(G):
    n=len(G)
    X=[0]
    T=[]
    W=[(0,float('inf')) for i in range(n)]
    while len(X)<n:
        edges=[]
        for i in range(n):
            if i not in X:
                for (j,c) in G[i]:
                    if j in X and W[i][1]>c:
                        W[i]=(j,c)
                edges.append((i,W[i][0],W[i][1]))
        edges.sort(key=lambda (x,y,z):z)
        i,j,w=edges[0]
        X.append(i)
        T.append(edges[0])
    return sum(e[2] for e in T)

def Heap_Prim_MST(G):
        n=len(G)
        X=[0]
        T=[]
        H=[(float('inf'),i,0) for i in range(1,n)]
        heapify(H)
        while len(X)<n:
            v=X[-1]
            for edge in G[v]:
                w=edge[0]
                if w not in X:
                    for e in H:
                        if e[1]==w:
                            if edge[1]<=e[0]:
                                H.remove(e)
                                H.append((edge[1],w,v))
            heapify(H)
            min_edge=heappop(H)
            X.append(min_edge[1])
            T.append((min_edge[1],min_edge[2],min_edge[0]))
        return sum(e[2] for e in T)





if __name__ == '__main__':
    start=clock()
    fname='edges.txt'
    #fname='PA2test3.txt'
    G=Load_data(fname)
    load_finish=clock()
    print 'Use',load_finish-start,'s to load data from the file'
    print 'Total Cost:',Naive_Prim_MST(G)
    naive_finish=clock()
    print 'Naive Prim method takes',naive_finish-load_finish,'s'
    print 'Total Cost:',Heap_Prim_MST(G)
    heap_finish=clock()
    print 'Prim Algorithm with heap takes',heap_finish-naive_finish,'s'
