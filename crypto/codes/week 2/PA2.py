from Crypto.Cipher import AES
from Crypto import Random
import Crypto.Util.Counter

BS=AES.block_size
def padding(text):
    n=BS-len(text)%BS
    padchar=chr(n)
    return text+n*padchar

def unpadding(text):
    n=ord(text[-1])
    return text[:len(text)-n]


def PA2CBCdecrypt(ciphertext,key):
    cstring=ciphertext.decode('hex')
    iv=cstring[:BS]
    k=key.decode('hex')
    cipher = AES.new(k, AES.MODE_CBC,iv)
    p=cipher.decrypt(cstring[BS:])
    return unpadding(p)

def PA2CTRdecrypt(ciphertext,key):
    cstring=ciphertext.decode('hex')
    iv=cstring[:BS]
    ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
    k=key.decode('hex')
    cipher = AES.new(k, AES.MODE_CTR,counter=ctr)
    p=cipher.decrypt(cstring[BS:])
    return p

k1='140b41b22a29beb4061bda66b6747e14'
c1='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
c2='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
k2='36f18357be4dbd77f050515c73fcf9f2'
c3='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
c4='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
print PA2CBCdecrypt(c1,k1)
print PA2CBCdecrypt(c2,k1)
print PA2CTRdecrypt(c3,k2)
print PA2CTRdecrypt(c4,k2)
