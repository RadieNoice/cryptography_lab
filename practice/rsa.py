import random,math
def key_generation():
    p=int(input("Enter p: "))
    q=int(input("Enter q: "))
    n=p*q
    phi_n=(p-1)*(q-1)
    e=random.randint(2,phi_n-1)#1<e<phi_n
    while(math.gcd(e,phi_n)!=1):
        e=random.randint(2,phi_n-1)
    d=pow(e,-1,phi_n)
    return d,e,n 
def signing(d,n):
    m=int(input("Enter message m: "))
    s=pow(m,d,n)
    return m,s
def verification(e,n,m,s):
    v=pow(s,e,n)
    print(v)
    print(m)
    return m==v

d,e,n=key_generation()
m,s=signing(d,n)
print(verification(e,n,m,s))