import hashlib
plaintext=input("Enter the plaintext: ")

sha_hash=hashlib.sha512(plaintext.encode()).hexdigest()
print(sha_hash)