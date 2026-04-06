import random
def key_generation():
    p=int(input("Enter prime p: "))
    q=int(input("Enter q st q|(p-1): "))
    g=random.randint(2,p-2)
    a=pow(g,(p-1)//q,p)
    xa=random.randint(1,q-1)#1<xa<q
    ya=pow(a,xa,p)
    return[p,q,a,xa,ya]
def signing(m,a,xa,p,q):
    k=random.randint(2,q-1)#1<k<q
    k_inv=pow(k,-1,q)
    s1=pow(a,k,p)%q
    s2=(k_inv*(m+xa*s1))%q
    return[m,s1,s2]

def verification(m,s1,s2,a,ya,p,q):
    w=pow(s2,-1,q)
    u1=m*w%q
    u2=s1*w%q
    v=(pow(a,u1)*pow(ya,u2)%p)%q
    return v==s1
m=int(input("Enter the message : "))
p,q,a,xa,ya=key_generation()
m,s1,s2=signing(m,a,xa,p,q)
print(verification(m,s1,s2,a,ya,p,q))
