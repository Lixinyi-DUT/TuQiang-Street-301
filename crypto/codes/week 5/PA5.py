import gmpy2
from gmpy2 import mpz


p=mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
g=mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
h=mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')


def buildleft():
    table=dict()
    for x_1 in range(0,(2**20)):
        gx=gmpy2.powmod(g,x_1,p)
        gx_inverse=gmpy2.invert(gx,p)
        if gx_inverse!=0:
            left=gmpy2.f_mod(gmpy2.mul(h,gx_inverse),p)
            table[left]=x_1
    return table

def rightsearch(table):
    gb=gmpy2.powmod(g,2**20,p)
    for x_0 in range(0,2**20):
        gx0=gmpy2.powmod(gb,x_0,p)
        if gx0 in table:
            print gmpy2.f_mod(gmpy2.add(gmpy2.f_mod(gmpy2.mul(x_0,(2**20)),p),table[gx0]),p)
            return x_0,table[gx0]
    print 'none'

if __name__ =='__main__':
    t=buildleft()
    print len(t)
    print rightsearch(t)
