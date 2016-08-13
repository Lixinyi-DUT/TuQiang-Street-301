def group(g,p):
    l=[1]
    t=1
    while True:
        t=t*g%p
        if t in l:
            return l
        else:
            l.append(t)


for i in range(1,5):
    print(group(i,5))

print(512%13)
