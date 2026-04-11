import math
def encrypt(text,a,b):
    text=text.lower().replace(" ","")
    result=""
    for i in text:
        result+=chr((a*(ord(i)-ord('a'))+b)%26+ord('a'))
    return result 

def decrypt(text,a,b):
    a_inv=pow(a,-1,26)
    result=""
    for i in text:
        result+=chr(((ord(i)-ord('a')-b)*a_inv)%26+ord('a'))
    return result 

m=input("Enter Message m: ")

a=int(input("Enter a: "))
while math.gcd(a,26)!=1:
    print(f"{a} and 26 are not coprimes")
    a=int(input("Enter another a: "))

b=int(input("Enter b: "))

cipher=encrypt(m,a,b)
print(cipher)

decrypted=decrypt(cipher,a,b)
print(decrypted)