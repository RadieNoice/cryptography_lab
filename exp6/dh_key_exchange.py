from sympy import nextprime
import random
p=int(input("Enter a number to find the next prime: "))
p=nextprime(p)
print(f"The prime is {p}")
p_r=[]
req_set=set(range(1,p))
for i in range(2,p):
    actual_set=set(pow(i,j,p)for j in range(1,p))
    if actual_set==req_set:
        p_r.append(i)
g=p_r[random.randint(0,len(p_r)-1)]
print(f"g={g}")
a=random.randint(1,p-1)
b=random.randint(1,p-1)
while b==a:
    b=random.randint(1,p-1)

print(f"alice secret key a={a}\nbob secret key b={b}")
def alice(g):
    return pow(g,a,p)
def bob(g):
    return pow(g,b,p)

A=alice(g)
B=bob(g)

print(f"alice A={A}\nbob B={B}")

sec_key_alice=alice(B)
sec_key_bob=bob(A)

print(f"alice shared secret key={sec_key_alice}\nbob shared secret key={sec_key_bob}")