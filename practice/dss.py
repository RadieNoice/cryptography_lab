import random,math
def key_generation():
    p=int(input("Enter primr p: "))
    q=int(input(f"Enter prime q st q | {p-1}: "))
    while True:
        g=random.randint(2,p-2) #1<g<p-1
        a=pow(g,(p-1)//q,p)
        if a>1:
            break
    xa=random.randint(1,q-1)
    ya=pow(a,xa,p)
    return a,xa,ya,p,q 

def signing(a,xa,p,q):
    m=int(input("Enter message m: "))
    k=random.randint(2,q-1)#1<k<q
    while(math.gcd(k,q)!=1):
         k=random.randint(2,q-1)
    k_inv=pow(k,-1,q)
    s1=pow(a,k,p)%q
    s2=(k_inv*(m+xa*s1))%q
    return m,s1,s2

def verification(a,ya,p,q,m,s1,s2):
    w=pow(s2,-1,q)
    u1=pow(m*w,1,q)
    u2=pow(s1*w,1,q)
    v=((pow(a,u1)*pow(ya,u2))%p)%q
    return v==s1

a,xa,ya,p,q=key_generation()
m,s1,s2=signing(a,xa,p,q)
print(verification(a,ya,p,q,m,s1,s2))  