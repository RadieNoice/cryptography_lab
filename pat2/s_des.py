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

def left_shift(bits,n):
    return bits[n:]+bits[:n]

def xor(a,b):
    return [x^y for x,y in zip(a,b)]

def sbox_lookup(bits,sbox):
    row=(bits[0]<<1)|bits[3]
    col=(bits[1]<<1)|bits[2]
    val=sbox[row][col]
    return [(val>>1)&1,val&1]

def generate_keys(keys):
    p10=permute(keys,P10)
    left,right=p10[:5],p10[5:]
    left,right=left_shift(left,1),left_shift(right,1)
    k1=permute(left+right,P8)
    left,right=left_shift(left,2),left_shift(right,2)
    k2=permute(left+right,P8)
    return k1,k2

def fk(bits,key):
    left,right=bits[:4],bits[4:]
    ep=permute(right,EP)
    xored=xor(ep,key)
    s0_out=sbox_lookup(xored[:4],S0)
    s1_out=sbox_lookup(xored[4:],S1)
    p4=permute(s0_out+s1_out,P4)
    return xor(left,p4)+right

def encryption(plaintext,key):
    k1,k2=generate_keys(key)
    ip=permute(plaintext,IP)
    after_fk1=fk(ip,k1)
    swapped=after_fk1[4:]+after_fk1[:4]
    after_fk2=fk(swapped,k2)
    return permute(after_fk2,IP_INV)

def decryption(cyphertext,key):
    k1,k2=generate_keys(key)
    ip=permute(cyphertext,IP)
    after_fk2=fk(ip,k2)
    swapped=after_fk2[4:]+after_fk2[:4]
    after_k1=fk(swapped,k1)
    return permute(after_k1,IP_INV)

key_str      = input("Enter 10-bit key (e.g. 1010000010): ")
plain_str    = input("Enter 8-bit plaintext (e.g. 11010111): ")

key       = [int(b) for b in key_str]
plaintext = [int(b) for b in plain_str]

ciphertext  = encryption(plaintext, key)
decrypted   = decryption(ciphertext, key)

print(f"Plaintext : {plain_str}")
print(f"Key       : {key_str}")
print(f"Ciphertext: {''.join(map(str, ciphertext))}")
print(f"Decrypted : {''.join(map(str, decrypted))}")