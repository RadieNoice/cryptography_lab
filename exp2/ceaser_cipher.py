m=list(input("Enter the message: "))
n=int(input("Enter n: "))

def encryption(m,n):
    e=[]
    for i in range(len(m)):
        e.append(chr((ord(m[i])-ord('a')+n)%26+ord('a')))
    return"".join(e)

def decryption(e,n):
    d=[]
    for i in range(len(e)):
        d.append(chr((ord(e[i])-ord('a')-n)%26+ord('a')))
    return "".join(d)
    
enc=encryption(m,n)
print("Encryption: ",enc)
dec=decryption(enc,n)
print("Decryption: ",dec)