def add(x,y,a,p):
    if x is None:
        return y
    if y is None:
        return x
    x1,y1=x
    x2,y2=y
    if(x1==x2 and (y2+y1)%p==0):
        return None
    if x1==x2 and y1==y2:
        s=((3*x1**2+a)*pow(2*y1,-1,p))%p
    else:
        s=((y2-y1)*pow(x2-x1,-1,p))%p 
    x3=(s**2-x1-x2)%p
    y3=(s*(x1-x3)-y1)%p
    return x3,y3

def mul(n,x,a,p):
    res=x
    for _ in range(n-1):
        res=add(res,x,a,p)
    return res 

def neg(x,p):
    return [x[0],(-x[1])%p]

def key_generation():
    a=int(input("Enter a: "))
    p=int(input("Enter p: "))
    d=int(input("Enter d: "))
    g1=int(input("Ener x of g: "))
    g2=int(input("Ener y of g: "))
    g=[g1,g2]
    q=mul(d,g,a,p)
    return d,g,q,a,p 

def encryption(q,g,a,p):
    m1=int(input("Ener x of m: "))
    m2=int(input("Ener y of m: "))
    m=[m1,m2]
    k=int(input("Enter k: "))
    s1=mul(k,g,a,p)
    s2=add(m,mul(k,q,a,p),a,p)
    return s1,s2
def decryption(d,a,p,c1,c2):
    return add(c2,neg(mul(d,c1,a,p),p),a,p)

d,g,q,a,p=key_generation()
s1,s2=encryption(q,g,a,p)
print(decryption(d,a,p,s1,s2))

# Enter a: 2
# Enter p: 17
# Enter d: 2
# Ener x of g: 5
# Ener y of g: 1
# Ener x of m: 6
# Ener y of m: 3
# Enter k: 3