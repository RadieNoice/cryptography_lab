import random 
def add(x,y,a,p):
    if x is None:
        return y 
    if y is None:
        return x 
    x1,y1=x
    x2,y2=y
    if x1==x2 and(y1+y2)%p==0:
        return None 
    if x1==x2 and y1==y2:
        s=((3*x1*x1+a)*pow(2*y1,-1,p))%p 
    else:
        s=((y2-y1)*pow(x2-x1,-1,p))%p 
    x3=(s*s-x1-x2 )%p 
    y3=(s*(x1-x3)-y1)%p 
    return [x3,y3]

def mul(n,x,a,p):
    res=x
    for i in range(n-1):
        res=add(res,x,a,p)
    return res

def neg(x,p):
    return [x[0],(-x[1])%p]

def order(x,a,p):
    q=x
    count=1
    while True:
        q=add(q,x,a,p)
        count+=1
        if q is None:
            break
    return count

def generate_point(a,b,p):
    res=[]
    for x in range(p):
        rhs=(x*x*x+a*x+b)%p
        for y in range(p):
            lhs=(y*y)%p
            if lhs==rhs:
                res.append([x,y])
    print(*res)

def key_generation():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    p=int(input("Enter p:"))
    generate_point(a,b,p)
    g=list(map(int,input("Enter base point g:").split()))
    n=order(g,a,p)
    d=random.randint(1,n-1)
    q=mul(d,g,a,p)
    return g,d,q,a,p

def encryption(g,q,a,p):
    n=order(g,a,p)
    k=random.randint(1,n-1)
    m=list(map(int,input("Enter message m as:").split()))
    c1=mul(k,g,a,p)
    c2=add(mul(k,q,a,p),m,a,p)
    return c1,c2

def decryption(c1,c2,a,d,p):
    return add(c2,neg(mul(d,c1,a,p),p),a,p)

g,d,q,a,p=key_generation()

c1,c2=encryption(g,q,a,p)

print(decryption(c1,c2,a,d,p))