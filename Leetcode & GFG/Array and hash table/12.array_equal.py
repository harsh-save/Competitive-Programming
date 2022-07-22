def check(A,B,N):
    ht={}
    for i in range(N):
        if(A[i] in B):
            ht[A[i]]=A[i]
    
    if len(ht)!=len(B):
        return 0
    return 1


print(check([16,1,2,14,13,17,1],[14,1,16,2,13,2,17],7))