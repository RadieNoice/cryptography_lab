import random,math
def key_generaration():
    p=int(input("Enter a prime p:"))
    q=int(input("Enter a prime q:"))
    n=p*q
    phi_n=(p-1)*(q-1)
    while True:
        e=random.randint(2,phi_n-1)
        if(math.gcd(e,phi_n)==1):
            break
    d=pow(e,-1,phi_n)
    return e,d,n
def encryption(e,n):
    m=int(input("Enter message m:"))
    return pow(m,e,n)

def decryption(d,n,c):
    return pow(c,d,n)

e,d,n=key_generaration()

cipher=encryption(e,n)
print(cipher)

decrypted=decryption(d,n,cipher)
print(decrypted)