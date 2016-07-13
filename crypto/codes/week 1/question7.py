import numpy as np
m1="attack at dawn"
m2="attack at dusk"
c1="6c73d5240a948c86981bc294814d"

def message2bit(string_text):
    bit_string=[]
    for char in string_text:
        bit_string.extend([int(d) for d in bin(ord(char))[2:].zfill(8)])
    return np.array(bit_string)

def hex2bit(string_text):
    dec=[int('0x'+c1[2*i:2*i+2],16) for i in range(len(string_text)/2)]
    bit_string=[]
    for i in dec:
        bit_string.extend([int(d) for d in bin(i)[2:].zfill(8)])
    return np.array(bit_string)

def binary_array_to_int(arr,l=len(c1)/2):
    arr=arr.reshape((l,8))
    return [int(''.join(i.astype(np.str)),2) for i in arr]

p1=message2bit(m1)
p2=message2bit(m2)
diff=p2-p1
pc1=hex2bit(c1)
pc2=(pc1+diff)%2
pc2num=binary_array_to_int(pc2)
c2=''.join([hex(i)[2:].zfill(2) for i in pc2num])
print c2
