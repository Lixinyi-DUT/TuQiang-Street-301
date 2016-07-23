import os
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def sort_and_count(A):
    length=len(A)
    if length > 1:
        X,B=sort_and_count(A[:length/2])
        Y,C=sort_and_count(A[length/2:])
        Z,D=CountSplitInv(B,C)
        return X+Y+Z,D
    else:
        return 0,A

# def CountSplitInv(B,C):
#     if len(B)>0 and len(C)>0:
#         if B[0] < C[0]:
#             c,d=CountSplitInv(B[1:],C)
#             return c, [B[0]]+d
#         else:
#             c,d=CountSplitInv(B,C[1:])
#             return c+len(B),[C[0]]+d
#     elif len(B)==0:
#         return 0,C
#     else:
#         return 0,B

def CountSplitInv(B,C):
    i=0
    j=0
    count=0
    D=[]
    while i<len(B) and j<len(C):
        if B[i]<C[j]:
            D.append(B[i])
            i=i+1
        else:
            D.append(C[j])
            j=j+1
            count=count+len(B[i:])
    if i==len(B):
            D=D+C[j:]
    else:
        D=D+B[i:]
    return count,D

fhand=open('IntegerArray.txt').read()
data=fhand.split()
array=[int(i) for i in data]

print sort_and_count(array)[0]
