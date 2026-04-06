import random,math
def key_generation():
    q=int(input("Enter a large prime q: "))
    a=int(input("Enter a primitive root alpha: "))
    xa=random.randint(2,q-1)
    ya=pow(a,xa,q)
    return [q,a,xa,ya]

def signing(q,a,xa,m):
    k=random.randint(1,q-2)#i<=k<q-1
    while(math.gcd(k,q-1)!=1):
        k=random.randint(1,q-2)#inclusive of 1 and q-2
    s1=pow(a,k,q)
    k_inv=pow(k,-1,q)
    s2=pow((m-xa*s1)*k_inv,1,q-1)
    return [m,s1,s2]

def verification(m,a,q,ya,s1,s2):
    v1=pow(a,m,q)
    v2=pow(pow(ya,s1)*pow(s1,s2),1,q)
    return v1==v2

q,a,xa,ya=key_generation()
m=int(input("Enter a message: "))
m,s1,s2=signing(q,a,xa,m)
print(verification(m,a,q,ya,s1,s2))