import gmpy2
from gmpy2 import mpz

N=mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')

(a,b)=gmpy2.isqrt_rem(N)
A=gmpy2.add(a,1)
A2=pow(A,2)
(x,d)=gmpy2.isqrt_rem(gmpy2.sub(A2,N))
if d==0:
    p=gmpy2.sub(A,x)
    q=gmpy2.add(A,x)
    if gmpy2.mul(p,q)==N:
        print p