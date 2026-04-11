import hashlib 
message=input("Enter the message: ")

sha_hash=hashlib.sha512(message.encode()).hexdigest()
print(sha_hash)
print(int(sha_hash,16)%100000000000000)