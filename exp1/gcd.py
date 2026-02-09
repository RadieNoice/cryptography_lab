def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


import math 
g=math.gcd(7,14)
print(g)
