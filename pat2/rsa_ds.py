import random,math
def key_generation():
    p=int(input("Enter a prime p: "))
    q=int(input("Enter a prime q: "))
    n=p*q
    phi_n=(p-1)*(q-1)
    e=random.randint(2,phi_n-1) #1<e<phi_n
    while(math.gcd(e,phi_n)!=1):
        e=random.randint(2,phi_n-1)
    d=pow(e,-1,phi_n)#private key
    return[n,e,d]
def signing(m,n,e):
    return [m,pow(m,e,n)]

def verification(m,s,d,n):
    m1=pow(s,d,n)
    return m==m1
n,e,d=key_generation()
m=int(input("ENter a message ie number: "))
m,s=signing(m,n,e)
print(verification(m,s,d,n))
