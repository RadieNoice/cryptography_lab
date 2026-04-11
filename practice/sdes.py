S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
P4  = [2,4,3,1]
IP  = [2,6,3,1,4,8,5,7]
IP_INV = [4,1,3,5,7,2,8,6]
EP  = [4,1,2,3,2,3,4,1]

def permute(bits,table):
    return [bits[i-1] for i in table]

def xor(a,b):
    return[x^y for x,y in zip(a,b)]

def s_box_lookup(bits,s_box):
    row=(bits[0]<<1)|bits[3]
    col=(bits[1]<<1)|bits[2]
    val=s_box[row][col]
    return [(val>>1)&1,val&1]

def left_shift(bits,n):
    return bits[n:]+bits[:n]

def key_generation(bits):
    bits=permute(bits,P10)
    left,right=bits[:5],bits[5:]
    left,right=left_shift(left,1),left_shift(right,1)
    k1=permute(left+right,P8)
    left,right=left_shift(left,2),left_shift(right,2)
    k2=permute(left+right,P8)
    return k1,k2

def fk(bits,key):
    left,right=bits[:4],bits[4:]
    ep=permute(right,EP)
    xored=xor(ep,key)
    s0=s_box_lookup(xored[:4],S0)
    s1=s_box_lookup(xored[4:],S1)
    p4=permute(s0+s1,P4)
    return xor(p4,left)+right

def encryption(bits,key):
    ip=permute(bits,IP)
    k1,k2=key_generation(key)
    fk1=fk(ip,k1)
    swapped=fk1[4:]+fk1[:4]
    fk2=fk(swapped,k2)
    ip_inv=permute(fk2,IP_INV)
    return ip_inv

def decryption(bits,key):
    ip=permute(bits,IP)
    k1,k2=key_generation(key)
    fk2=fk(ip,k2)
    swapped=fk2[4:]+fk2[:4]
    fk1=fk(swapped,k1)
    ip_inv=permute(fk1,IP_INV)
    return ip_inv

key_str      = "1010000010"
plain_str    = "dhilip"

key       = [int(b) for b in key_str]
plaintext = [(ord(b)-ord('a')) for b in plain_str]
plaintext=[[int(b) for b in format(i,"08b")]for i in plaintext]
print(plaintext)
print(''.join(chr(int(''.join(str(b)for b in bits),2)+ord('a')) for bits in plaintext))
ciphertext  = [encryption(i, key)for i in plaintext]
decrypted   = [decryption(i, key)for i in ciphertext]
print(f"Plaintext : {plain_str}")
print(f"Key       : {key_str}")
print(f"Ciphertext: {ciphertext}")
print(''.join(chr(int(''.join(str(b)for b in bits),2)+ord('a')) for bits in ciphertext))
print(f"Decrypted: {decrypted}")
print(''.join(chr(int(''.join(str(b)for b in bits),2)+ord('a')) for bits in decrypted))
# print(f"Ciphertext: {''.join(map(str, ciphertext))}")
# print(f"Decrypted : {''.join(map(str, decrypted))}")