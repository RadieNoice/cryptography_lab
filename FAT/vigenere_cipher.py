def encrypt(text,key):
    text=text.lower()
    key=key.lower()
    result=""
    for i in range(len(text)):
        x=ord(text[i])-ord('a')
        y=ord(key[i])-ord('a')
        result+=chr((x+y)%26+ord('a'))
    return result 

def decrypt(text,key):
    key=key.lower()
    result=""
    for i in range(len(key)):
        x=ord(text[i])-ord('a')
        y=ord(key[i])-ord('a')
        result+=chr((x-y)%26+ord('a'))
    return result 

m=input("Enter Mesaage m: ")
k=input("Enter key: ")

if len(k)>=len(m):
    k=k[:len(m)]
else:
    i=0
    while len(k)!=len(m):
        k+=k[i%len(k)]
        i+=1
print(k)

cipher=encrypt(m,k)
print(cipher)

decrypted=decrypt(cipher,k)
print(decrypted)