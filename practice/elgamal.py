import random,math,hashlib
def primitive_roots(q):
    req=set(range(1,q))
    ans=[]
    for i in range(1,q):
        roots=set([pow(i,j,q) for j in range(1,q)])
        if(req==roots):
            ans.append(i)
    print(ans)
def key_generation():
    q=int(input("Enter a prime q: "))
    primitive_roots(q)
    a=int(input("Enter the primitve root alpha: "))
    xa=random.randint(2,q-2)
    ya=pow(a,xa,q)
    return a,xa,ya,q
def signing(a,xa,q):
    m=(input("Enter a message m: "))
    m1=m
    m=int(hashlib.sha512(m.encode()).hexdigest(),16)%(q)
    k=random.randint(2,q-1)
    while(math.gcd(k,q-1)!=1):
        k=random.randint(2,q-2)
    k_inv=pow(k,-1,q-1)
    s1=pow(a,k,q)
    s2=k_inv*(m-xa*s1)%(q-1)
    return m1,s1,s2

def verification(a,ya,q,m,s1,s2):
    m=int(hashlib.sha512(m.encode()).hexdigest(),16)%(q)
    v1=pow(a,m,q)
    v2=(pow(ya,s1,q)*pow(s1,s2,q))%q
    return v1==v2
a,xa,ya,q=key_generation()
m,s1,s2=signing(a,xa,q)
print(verification(a,ya,q,m,s1,s2))