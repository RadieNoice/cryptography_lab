def mod_inverse(a,m):
    try:
        return pow(a,-1,m)
    except ValueError:
        return None
    
def matrix_inv(m):
    a,b=m[0]
    c,d=m[1]
    det=(a*d-b*c)%26
    det_inv=mod_inverse(det,26)
    if det_inv!=None:
        return [[(d*det_inv)%26,(-b*det_inv)%26],
                [(-c*det_inv)%26,(a*det_inv)%26]]
    else:
        return None

def encrypt(text,k):
    text=text.lower().replace(" ","")
    if len(text)%2!=0:
        text+="x"
    result=""
    a,b=k[0]
    c,d=k[1]
    for i in range(0,len(text),2):
        p0=ord(text[i])-ord('a')
        p1=ord(text[i+1])-ord('a')
        c1=(a*p0+b*p1)%26
        c2=(c*p0+d*p1)%26
        result+=chr(c1+ord('a'))+chr(c2+ord('a'))
    return result

def decryt(text,k):
    k_inv=matrix_inv(k)
    return encrypt(text,k_inv)

m=input("Enter message m: ")

k=[[3,3],[2,5]]
cipher=encrypt(m,k)
print("Cipher Text:",cipher)

decrypted=decryt(cipher,k)
print("Decrypted:",decrypted)
