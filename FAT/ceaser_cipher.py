def encrypt(text,k):
    text=text.lower().replace(" ","")
    result=""
    for i in text:
        result+=chr((ord(i)-ord('a')+k)%26+ord('a'))
    return result 

def decrypt(text,k):
    result=""
    for i in text:
        result+=chr((ord(i)-ord('a')-k)%26+ord('a'))
    return result

m=input("Enter message m: ")
k=int(input("Enter k: "))

cipher=encrypt(m,k)
print(cipher)

decipher=decrypt(cipher,k)
print(decipher)
