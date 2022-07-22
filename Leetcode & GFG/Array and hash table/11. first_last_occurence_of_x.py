def occ(arr,n,x):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i] == x:
            first=i
            break
        
    
    for i in range(n-1,0,-1):
        if arr[i] == x:
            last=i
            break
    if(first==last):
        return 0,0
    if(first!=-1 and last!=-1):
        return first, last
    

print(occ([1,8],2,8))