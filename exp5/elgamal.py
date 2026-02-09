import random
from random import getrandbits
from sympy import nextprime
q=int(input("Enter a prime: "))
# q=getrandbits(1024)
q=nextprime(q)
print(f"prime q={q}")
m=int(input("Enter message: "))

def prime_factors(n):
    factors=set()
    i=2
    while i*i<=n:
        while n%i==0:
            factors.add(i)
            n//=i
        i+=1
    if n>1:
        factors.add(n)
    return factors
def primitive_roots(q):
    factors=prime_factors(q-1)
    for g in range(2,q):
        for p in factors:
            if pow(g,(q-1)//p,q)==1:
                break
        else:
            return g
# def primitive_roots(q):
#     p_r=[]
#     req_set=set(range(1,q))
#     for i in range(2,q):
#         actual_set=set(pow(i,j,q) for j in range(1,q))
#         if req_set==actual_set:
#             print (i)
#             break
#     #print(p_r[random.randint(0,len(p_r)-1)])

a=primitive_roots(q)
xa=random.randint(2,q-1)
ya=pow(a,xa,q)

print(f"Pulic key q={q} ya={ya} alpha={a}")
def encryption(m,q):
    k=random.randint(2,q-1)
    c1=pow(a,k,q)
    K=pow(ya,k,q)
    c2=pow(m*K,1,q)
    return c1,c2

def decryption(c1,c2,q):
    K=pow(c1,xa,q)
    k_inv=pow(K,-1,q)
    return pow(c2*k_inv,1,q)

c1,c2=encryption(m,q)
print(f"c1={c1} c={c2}")
d=decryption(c1,c2,q)
print(f"decryption: {d}")
