import random ,math
# p=int(input("Enter 1st prime: "))
# q=int(input("Enter 2nd prime: "))
from sympy import nextprime
from random import getrandbits
x=getrandbits(1024)
p=nextprime(x)
q=nextprime(p)
print(f"Keys p={p}\n\nq={q}")
m=int(input("Enter integer: "))

def key_generation(p,q):
    n=p*q
    phi_n=(q-1)*(p-1)
    while(True):
        e=random.randint(2,phi_n-1)
        if math.gcd(e,phi_n)==1:
            break
    return e,n,phi_n

def encryption(e,n,m):
    return pow(m,e,n)

def decryption(c,e,n,phi_n):
    d=pow(e,-1,phi_n)
    return pow(c,d,n)

e,n,phi_n=key_generation(p,q)
print(f"\nPublic key e={e}\n\nn={n}\n")
enc=encryption(e,n,m)
print(f"Encryption: {enc}\n")
dec=decryption(enc,e,n,phi_n)
print(f"Decryption: {dec}")