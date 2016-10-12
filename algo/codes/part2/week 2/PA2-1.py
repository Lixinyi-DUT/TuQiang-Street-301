import os
from time import clock
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 2')

def load_data(fname):
    edges=[]
    fhand=open(fname)
    for line in fhand:
        d=line.split()
        if len(d)==1:
            n=int(d[0])
        if len(d)==3:
            edges.append((int(d[0])-1,int(d[1])-1,int(d[2])))
    return edges,n

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

def k_clusterings(edges,n,k):
    leader=[i for i in range(n)]
    edges.sort(reverse=True,key=lambda (x,y,z):z)
    while len(set(leader)) !=k and len(edges)>0:
        e=edges.pop()
        while leader[e[0]]==leader[e[1]]:
            e=edges.pop()
        leader=leader_update(leader,n,leader[e[0]],leader[e[1]])
    e=edges.pop()
    while leader[e[0]]==leader[e[1]]:
        e=edges.pop()
    return e[2] # return minimum distance between different clusters

if __name__ == '__main__':
    fname='clustering1.txt'
    #fname='PA1test2.txt'
    start=clock()
    edges,n=load_data(fname)
    load_finish=clock()
    print load_finish-start,'s for loading data from file'
    space=k_clusterings(edges,n,4)
    cluster_finish=clock()
    print space
    print cluster_finish-load_finish,'s for clustering'
