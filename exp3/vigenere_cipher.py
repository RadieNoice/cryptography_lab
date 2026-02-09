m=input("Enter message: ").lower()
k=input("Enter keyword: ").lower()

if(len(k)<len(m)):
    x=len(m)-len(k)
    y=len(k)
    for i in range(x):
        k+=k[i%y]
elif(len(k)>len(m)):
    k=k[:len(m)]
print("Modified key: ",k)

def encryption(m,k):
    e=""
    for i in range(len(m)):
        e+=chr((ord(m[i])+ord(k[i])-2*ord('a'))%26+ord('a'))
    return e

def decryption(e,k):
    d=""
    for i in range(len(e)):
        d+=chr((ord(e[i])-ord(k[i]))%26+ord('a'))
    return d

enc=encryption(m,k)
print("Encryption: ",enc)
dec=decryption(enc,k)
print("Decryption: ",dec)