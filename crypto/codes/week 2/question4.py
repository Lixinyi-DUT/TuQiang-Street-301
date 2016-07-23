def str_int_xor(a, b):
    return "".join([chr(ord(x) ^ y) for (x, y) in zip(a, b)])

output1='e86d2de2 e1387ae9'
output2='1792d21d b645c008'

# output1='7c2822eb fdc48bfb'
# output2='325032a9 c5e2364b'

# output1='4af53267 1351e2e1'
# output2='87a40cfa 8dd39154'

# output1='2d1cfa42 c0b1d266'
# output2='eea6e3dd b2146dd0'

l0_1=[0 for i in range(4)]
r0_1=[0 for i in range(4)]
l0_2=[255 for i in range(4)]
r0_2=[0 for i in range(4)]

o1=output1.split()
l2_1=o1[0].decode('hex')
r2_1=o1[1].decode('hex')

o2=output2.split()
l2_2=o2[0].decode('hex')
r2_2=o2[1].decode('hex')

f_k1_r0_1=str_int_xor(l2_1,l0_1)
f_k1_r0_2=str_int_xor(l2_2,l0_2)
# f_k2_r1_1=str_int_xor(r2_1,r0_1)
# f_k2_r1_2=str_int_xor(r2_2,r0_2)



print [ord(i) for i in f_k1_r0_1]
print [ord(i) for i in f_k1_r0_2]
