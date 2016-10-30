n=7
a=[0 for i in range(n+1)]
A=[list(a) for i in range(n+1)]
#p=[5,40,8,4,10,10,23]
p=[20,5,17,10,20,3,25]

def updata_node(A,i,s,p):
    v=[]
    for r in range(i,i+s+1):
        x=sum(p[i:i+s+1])+A[i][r-1]+A[r+1][i+s]
        v.append(x)
    return min(v)

for s in range(n+1):
    for i in range(n):
        if i+s<n:
            A[i][i+s]=updata_node(A,i,s,p)


print A[0][6]
