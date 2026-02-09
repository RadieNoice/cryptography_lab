m=input("Enter the message: ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))

def encryption(m,a,b):
    e=[]
    for i in range(len(m)):
        e.append(chr(((ord(m[i])-ord('a'))*a+b)%26+ord('a')))
    return "".join(e)

def decryption(e,a,b):
    a_inv=pow(a,-1,26)
    d=[]
    for i in range(len(e)):
        d.append(chr((((ord(e[i])-ord('a'))-b)*a_inv)%26+ord('a')))
    return "".join(d)

enc=encryption(m,a,b)
print("Encryption: ",enc)
dec=decryption(enc,a,b)
print("Decryption: ",dec)