def add(x,y,a,p):
    if x is None:
        return y
    if y is None:
        return x
    x1,y1=x
    x2,y2=y
    if x1==x2 and (y1+y2)%p==0:
        return None
    if x1==x2 and y1==y2:
        s=pow((3*x1**2+a)*pow(2*y1,-1,p),1,p)
    else:
        s=pow((y2-y1)*pow(x2-x1,-1,p),1,p)

    x3=pow(s**2-x1-x2,1,p)
    y3=pow(s*(x1-x3)-y1,1,p)
    return [x3,y3]
def mul(n,x,a,p):
    res=x
    for i in range(n-1):
        res=add(res,x,a,p)
    return res
def neg(x,p):
    return [x[0],(-x[1])%p]
a=int(input("enetr a: "))
b=int(input("enetr b: "))
p=int(input("enetr p: "))

x=int(input("enetr x: "))
y=int(input("enetr y: "))
g=[x,y]
d=int(input("Enter private key d:")) 
q=mul(d,g,a,p)

def encryption(a,p,m,g,q):
    k=int(input("enter value for k: "))
    c1=mul(k,g,a,p)
    c2=add(m,mul(k,q,a,p),a,p)
    return c1,c2
def decryption(d,a,p,c1,c2):
    return add(c2,neg(mul(d,c1,a,p),p),a,p)

m1=int(input("enter x coordinate of m:"))
m2=int(input("enter y coordinate of m:"))
m=[m1,m2]
c1,c2=encryption(a,p,m,g,q)
print(decryption(d,a,p,c1,c2))