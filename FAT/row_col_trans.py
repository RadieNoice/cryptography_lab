import math
def encryption(text,key):
    result=""
    text=text.lower().replace(" ","")
    col=len(key)
    row=math.ceil(len(text)/col)
    matrix=[['x' for i in range(col)]for j in range(row)]
    idx=0
    for i in range(row):
        for j in range(col):
            if(idx>=len(text)):
                break
            matrix[i][j]=text[idx]
            idx+=1
    for i in key:
        for j in range(row):
            result+=matrix[j][i]
    return result 

def decryption(text,key):
    result=""
    col=len(key)
    row=math.ceil(len(text)/col)
    matrix=[['x' for i in range(col)]for j in range(row)]
    idx=0 
    for i in key:
        for j in range(row):
            matrix[j][i]=text[idx]
            idx+=1
    
    for i in range(row):
        for j in range(col):
            result+=matrix[i][j]
    return result 

m=input("Enter message m: ")
m=m.lower().replace(" ","")
k=[i for i in map(int,input("Enter Key order:").split())]
print(math.ceil(len(m)/len(k)))
cipher=encryption(m,k)
print(cipher)

decrypted=decryption(cipher,k)
print(decrypted)