import math
m=input("Enter the message: ")

def encryption(m):
    x=math.ceil(math.sqrt(len(m)))
    print(f"message size:{len(m)}\nmatrix size {x}x{x}")
    matrix=[['$' for j in range(x)]for i in range(x)]
    y=0
    for i in range(x):
        for j in range(x):
            if(y<len(m)):
                matrix[i][j]=m[y]
                y+=1
    return "".join(matrix[i][j] for j in range(x) for i in range(x)),x
        
def decryption(e,x):
    matrix=[[' ' for j in range(x)]for i in range(x)]
    y=0
    for i in range(x):
        for j in range(x):
            matrix[j][i]=e[y]
            y+=1

    return "".join(matrix[j][i] for j in range(x) for i in range(x))

enc,x=encryption(m)
print("Encryption: ",enc)
dec=decryption(enc,x)
print("Decryption: ",dec)