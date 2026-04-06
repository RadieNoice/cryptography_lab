import hashlib 
plaintext=input("Enter your message: ")
md5_hash=hashlib.md5(plaintext.encode()).hexdigest()
print(md5_hash)