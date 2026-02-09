m=input("Enter the message: ")
k=input("Enter the keyword: ")

#keyword processing
seen=set()
x=[]
for i in k:
    if not i.isalpha():
        continue
    if i=='j':
        i='i'
    if i not in seen:
        seen.add(i)
        x.append(i)
k=x

#playfair matrix making
matrix=[['x'for j in range(5)]for i in range (5)]
alphabet=[0 for i in range(26)]
for i in k:
    alphabet[ord(i)-ord('a')]=1

alphabet[ord('j')-ord('a')]=1 #always make j as 1 ie skip j 
r=""
for i in range(26):
    if alphabet[i]==0:
        r+=chr(i+ord('a'))
y=0
z=0
for i in range(5):
    for j in range(5):
        if y<len(k):
            matrix[i][j]=k[y]
            y+=1
        elif z<len(r):
            matrix[i][j]=r[z]
            z+=1
        else:
            break

for i in range(5):
    for j in range(5):
        print(matrix[i][j]," ",end=" ")
    print("")

def pos(x,matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==x:
                return i,j

def encryption(m,matrix):
    #preprocessing m 
    #for repeating char in plaintext
    i=0
    while i<len(m)-1:
        if m[i]==m[i+1]:
            m=m[:i+1]+'x'+m[i+1:]
        if m[i]=='j':
            m=m[:i]+'i'+m[i+1:]
        i+=2
    if len(m)%2!=0:
        m+='x'
    print(m)
    e=""
    for i in range(0,len(m)-1,2):
        x1,y1=pos(m[i],matrix)
        x2,y2=pos(m[i+1],matrix)
        if x1==x2:
            e+=matrix[(x1+1)%5][y1]+matrix[(x2+1)%5][y2]
        elif y1==y2:
            e+=matrix[x1][(y1+1)%5]+matrix[x2][(y2+1)%5]
        else:
            e+=matrix[x1][y2]+matrix[x2][y1]
    print(len(m))
    print(len(e))
    return e
def decryption(e,matrix):
    d=""
    for i in range(0,len(e)-1,2):
        x1,y1=pos(e[i],matrix)
        x2,y2=pos(e[i+1],matrix)
        if x1==x2:
            d+=matrix[(x1-1)%5][y1]+matrix[(x2-1)%5][y2]
        elif y1==y2:
            d+=matrix[x1][(y1-1)%5]+matrix[x2][(y2-1)%5]
        else:
            d+=matrix[x1][y2]+matrix[x2][y1]
    return d

enc=encryption(m,matrix)
print(f"Encryption: {enc}")
dec=decryption(enc,matrix)
print(f"Decryption: {dec}")