import os
import threading
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

t=0

def DFS1(G,i):
    global marked,t,f
    visit=[i]
    while len(visit)>0:
        k=visit.pop()
        temp=[]
        for u in G[k]:
            if marked[u]==0 and u not in visit:
                temp.append(u)
        if len(temp)>0:
            visit.append(k)
            visit=visit+temp
        else:
            marked[k]=1
            t=t+1
            f[k]=t
            print(k,t)

def DFS2(G,s,i):
    global marked,leader,t
    visit=[i]
    while len(visit)>0:
        k=visit.pop()
        temp=[]
        for u in G[k]:
            if marked[u]==0 and u not in visit:
                temp.append(u)
        if len(temp)>0:
            visit.append(k)
            visit=visit+temp
        else:
            leader[k]=s
            marked[k]=1
            t=t-1
            print(k,t)

def DFS_loop1(G,n):
    global t,f,marked
    marked=[0 for i in range(n)]
    f=[0 for i in range(n)]
    for i in range(n):
        if marked[i]==0:
            print(i)
            DFS1(G,i)

def DFS_loop2(G,n,order):
    global marked,leader
    leader=list(range(n))
    marked=[0 for i in range(n)]
    for i in order:
        if marked[i]==0:
            print(i)
            print(i)
            s=i
            DFS2(G,s,i)


def dataread(fname,n):
    fhand=open(fname)
    G=[[] for i in range(n)]
    Grev=[[] for i in range(n)]
    for line in fhand:
        if len(line)>2:
            temp=line.split()
            a=int(temp[0])-1
            b=int(temp[1])-1
            G[a].append(b)
            Grev[b].append(a)
    fhand.close()
    return G,Grev

def kosaraju():
    global marked,t,f,leader
    n=875714
    fname='PA4data.txt'
    (G,Grev)=dataread(fname,n)
    DFS_loop1(Grev,n)
    ndown=[b for (a,b) in sorted(zip(f,list(range(n))),reverse=True)]
    DFS_loop2(G,n,ndown)
    count=dict()
    print(leader)
    for i in leader:
        count[i]=count.get(i,0)+1
    print sorted(count.values(),reverse=True)[0:5]

if __name__ =='__main__':
    thread=threading.Thread(target=kosaraju)
    thread.start()
