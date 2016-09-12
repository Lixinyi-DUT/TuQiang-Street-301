import os
os.chdir(r'F:\TuQiang-Street-301\algo\codes\part2\week 1')


def Load_data(fname):
    fhand=open(fname)
    data=[]
    for lines in fhand:
        info=lines.split()
        if len(info)>1:
            data.append((int(info[0]),int(info[1])))
    return data

def Complete_time(sche):
    cost=0
    time=0
    for job in sche:
        time=time+job[1]
        cost=cost+job[0]*time
    return cost

if __name__ =='__main__':
    fname='jobs.txt'
    #fname='PA1test3.txt'
    d=Load_data(fname)
    schedule1=sorted(d,key=lambda (x,y):(x-y,x), reverse=True) #sorted by largest differance=weight-length, when coming across the same differance, sorted by largest weight to break ties.
    schedule2=sorted(d,key=lambda (x,y):float(x)/y, reverse=True) #sorted by largest ratio=weight/length
    print 'Differance:',Complete_time(schedule1)
    print 'Ratio:',Complete_time(schedule2)
