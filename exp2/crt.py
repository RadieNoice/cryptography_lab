import math
n=int(input("Enter n: "))
r=[]
m=[]
M=1
x=0
for i in range(n):
    r.append(int(input()))
for i in range(n):
    m.append(int(input()))
    M*=m[i]

for i in range(n):
    for j in range(i+1,n):
        if math.gcd(m[i],m[j])!=1:
            raise ValueError("CRT not applicable: moduli not coprime")
for i in range(n):
    Mi=M//m[i]
    Mi_inv=pow(Mi,-1,m[i])
    x+=r[i]*Mi_inv*Mi

print("x=",pow(x,1,M))