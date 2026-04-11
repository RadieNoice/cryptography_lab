import math 
n=int(input("Enter n:"))
print("Enter remainders:")
s=input()
a=[i for i in map(int,s.split())]
print("Enter moduli's:")
s=input()
m=[i for i in map(int,s.split())]
M=1
for i in m:
    M*=i

def valid(m):
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(m[i],m[j])!=1:
                return False
    return True

if valid(m):
    x=0
    for i in range(n):
        Mi=M//m[i]
        Mi_inv=pow(Mi,-1,m[i])
        x+=a[i]*Mi*Mi_inv
    x%=M
    print(x)
    print("verification:")
    for i in range(n):
        print(f"{x}%{m[i]}={x%m[i]} and actual remainder is {a[i]}")
else:
    print("Invalid moduli")