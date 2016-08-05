s='20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d'

x='Pay Bob 100$'.find('1')
orginal=s[x*2:x*2+2]

changed=chr(ord(orginal.decode('hex'))^ord('1')^ord('5')).encode('hex')
print s[0]
print s[:x*2]+changed+s[(x*2+2):]
