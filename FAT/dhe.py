import random
def primitive_roots(n):
    req=set(range(1,n))
    result=[]
    for i in range(1,n):
        actual=set([pow(i,j,n)for j in range(1,n)])
        if req==actual:
            result.append(i)
    print(*result)

def key_generation():
    q=int(input("Enter a prime q:"))
    primitive_roots(q)
    a=int(input("choose a primitive root a:"))
    k1=random.randint(1,q-2)
    while True:
        k2=random.randint(1,q-2)
        if k1!=k2:
            break
    return q,a,k1,k2
def alice(a,k1,q):
    return pow(a,k1,q)
def bob(a,k2,q):
    return pow(a,k2,q)

q,a,k1,k2=key_generation()
A=alice(a,k1,q)
B=bob(a,k2,q)

SS_A=alice(B,k1,q)
SS_B=bob(A,k2,q)

print(SS_A)
print(SS_B)