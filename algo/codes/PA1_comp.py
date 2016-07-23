import os
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def sort_and_count(A):
    count=0
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                count=count+1
    return count


fhand=open('IntegerArray.txt').read()
data=fhand.split()
array=[int(i) for i in data]
print sort_and_count(array)
