import numpy as np
from sympy import Matrix
import math 
m=input("enetr message: ")
k=Matrix([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

def make_matrix(m,n):
    matrix=[ord('x')-ord('a')  for _ in range(n)]
    x=0
    for i in range(n):
        if x<len(m):
            matrix[i]=m[x]
            x+=1
        else:
            break
    return Matrix(matrix)
def encryption(m,key):
    n=key.shape[0]
    txt=[ord(i)-ord('a')for i in m]
    e=""
    for i in range(0,len(txt),n):
        block=make_matrix(txt[i:i+n],n)
        result=(key*block)%26
        e+="".join([chr(i+ord('a')) for i in result])
    return e

def decryption(e,key):
    n=key.shape[0]
    txt=[ord(i)-ord('a')for i in e]
    k_inv=key.inv_mod(26)
    d=""
    for i in range(0,len(m),n):
        block=make_matrix(txt[i:i+n],n)
        result=(k_inv*block)%26
        d+="".join([chr(i+ord('a')) for i in result])
    return d

enc=encryption(m,k)
print(f"Encryption: {enc}")
dec=decryption(enc,k)
print(f"Decryption: {dec}")