def primitive_roots(q):
    p_r=[]
    req_set=set(range(1,q))
    for i in range(2,q):
        actual_set=set(pow(i,j,q) for j in range(1,q))
        if req_set==actual_set:
            print (i)
            break
    #print(p_r[random.randint(0,len(p_r)-1)])

def isprime(n):
    if n<2:
        return False
    if(n==2):
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True

def next_prime(n):
    ans=n
    while True:
        n+=1
        if isprime(n):
            ans=n
            break
    return ans

n=int(input("Enter: "))
print(next_prime(n))