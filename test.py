def primitive_roots(q):
    p_r=[]
    req_set=set(range(1,q))
    for i in range(2,q):
        actual_set=set(pow(i,j,q) for j in range(1,q))
        if req_set==actual_set:
            print (i)
            break
    #print(p_r[random.randint(0,len(p_r)-1)])
