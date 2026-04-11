import random ,math
def primitive_roots(n):
    req=set(range(1,n))
    result=[]
    for i in range(1,n):
        actual=set([pow(i,j,n)for j in range(1,n)])
        if req==actual:
            result.append(i)
    print(*result)

def key_generation():
    q=int(input("Enter large q:"))
    primitive_roots(q)
    a=int(input("Choose one of the primitive roots: "))
    xa=random.randint(1,q-2)
    ya=pow(a,xa,q)
    return a,xa,ya,q

def encryption(a,ya,q):
    m=int(input("Enter Message m:"))
    k=random.randint(1,q-1)
    c1=pow(a,k,q)
    c2=(pow(ya,k,q)*m)%q
    return c1,c2

def decryption(a,xa,q,c1,c2):
    K=pow(c1,xa,q)
    K_inv=pow(K,-1,q)
    return (K_inv*c2)%q
a,xa,ya,q=key_generation()

c1,c2=encryption(a,ya,q)
print(decryption(a,xa,q,c1,c2))