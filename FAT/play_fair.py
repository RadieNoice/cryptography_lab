m=input("Enter message m: ").lower().replace('j','i')
k=input("Enter Keyword k: ").lower().replace('j','i')

seen=set()
key=[]
for i in k:
    if i not in seen:
        seen.add(i)
        key.append(i)

used=set(key)
used.add('j')

remaining=[]
for i in range(26):
    ch=chr(i+ord('a'))
    if ch not in used:
        used.add(ch)
        remaining.append(ch)

full=key+remaining

matrix=[[''for i in range(5)]for j in range(5)]
idx=0
for i in range(5):
    for j in range(5):
        matrix[i][j]=full[idx]
        idx+=1
    
print("\nPlayfair Matrix:")
for row in matrix:
    print(' '.join(row))

def preprocessing(text):
    result=""
    i=0
    while(i<len(text)):
        a=text[i]
        if i+1<len(text):
            b=text[i+1]
            if(a==b):
                result+=a+'x'
                i+=1
            else:
                result+=a+b
                i+=2
        else:
            result+=a+'x'
            i+=1
    return result

def pos(c,matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==c:
                return i,j
    return -1,-1

def encryption(text,matrix):
    text=preprocessing(text)
    result=""
    for i in range(0,len(text),2):
        x1,y1=pos(text[i],matrix)
        x2,y2=pos(text[i+1],matrix)
        if x1==x2:
            result+=matrix[x1][(y1+1)%5]+matrix[x2][(y2+1)%5]
        elif y1==y2:
            result+=matrix[(x1+1)%5][y1]+matrix[(x2+1)%5][y2]
        else:
            result+=matrix[x1][y2]+matrix[x2][y1]
    return result 

def decryption(text,matrix):
    result=""
    for i in range(0,len(text),2):
        x1,y1=pos(text[i],matrix)
        x2,y2=pos(text[i+1],matrix)
        if x1==x2:
            result+=matrix[x1][(y1-1)%5]+matrix[x2][(y2-1)%5]
        elif y1==y2:
            result+=matrix[(x1-1)%5][y1]+matrix[(x2-1)%5][y2]
        else:
            result+=matrix[x1][y2]+matrix[x2][y1]
    return result

cipher=encryption(m,matrix)
print(cipher)

decrypted=decryption(cipher,matrix)
print(decrypted)