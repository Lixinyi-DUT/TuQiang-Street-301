import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
bsize=16
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
def query(q):
    target = TARGET + urllib2.quote(q.encode('hex'))    # Create query URL
    req = urllib2.Request(target)       # Send HTTP request to server
    try:
        f = urllib2.urlopen(req)          # Wait for response
    except urllib2.HTTPError, e:
        print "We got: %d" % e.code       # Print response code
        if e.code == 404:
            return True # good padding
        return False # bad padding

def str_replace(string,i,x):
    ch=string[i]
    new_q=chr(ord(ch)^x)
    new_string=string[:i]+new_q+string[i+1:]
    return new_string


def guess(q,g,i):
    n=int(i/bsize)
    pad=(16-i%bsize)
    for j in range(i+1,(n+1)*bsize):
        q=str_replace(q,j,pad)
    print pad^g
    print chr(ord(q[i])).encode('hex')
    print chr(ord(q[i])^pad^g).encode('hex')
    q=str_replace(q,i,pad^g)
    print q.encode('hex')
    return q

def lastbyte(q,i):
    for g in range(256):
        if query(guess(q,g,i)):
            c=q
            for j in range(i-g+2,i+1):
                c=str_replace(c,j,g)
            return (g,c)


ciphertext='f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

cipher=ciphertext.decode('hex')
(n,c)=lastbyte(cipher,47)

print c.encode('hex')
print ciphertext

message=[ord(' ') for i in range(48-n)]
for i in range(48-n,47-n,-1):
    if (i+1)%bsize==0:
        c=cipher[:(int(i/bsize)+2)*bsize]
    for g in range(10):
        if query(guess(c,g,i)):
            message[i]=g
            print ''.join([chr(x) for x in message])
            c=str_replace(c,i,g)
            break
        print ciphertext
        print i,'error guess:',g
