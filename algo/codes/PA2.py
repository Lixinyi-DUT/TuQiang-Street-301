import os
os.chdir(r'F:\TuQiang-Street-301\algo\codes')

def median(array):
    length=len(array)
    first,middle,final=array[0],array[int((length+1)/2)-1],array[-1]
    l=sorted([first,middle,final])
    if first==l[1]:
        return 0
    if middle==l[1]:
        return int((length+1)/2)-1
    else:
        return -1


def partition(array,p):
    x=array[p]
    if p!=0:
        array[p],array[0]=array[0],array[p]
    i=1
    for j in range(1,len(array)):
        if array[j]<x:
            array[j],array[i]=(array[i],array[j])
            i=i+1
    array[0],array[i-1]=array[i-1],array[0]
    return array,i-1

def quicksort(array):
    length=len(array)
    if length<2:
        return array,0
    else:
        a,p=partition(array,median(array))
        l,c1=quicksort(a[:p])
        r,c2=quicksort(a[p+1:])
        return l+[array[p]]+r,c1+c2+length-1

fhand=open('PA2array.txt').read()
data=fhand.split()
array=[int(i) for i in data]
print quicksort(array)
