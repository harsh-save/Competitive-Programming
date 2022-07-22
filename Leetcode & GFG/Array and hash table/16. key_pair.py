def hasArrayTwoCandidates(arr, n, x):
    hashtable={}
    res=[]
    for i in range(n):
        k=abs(x-arr[i])
        if k in hashtable:

            res.append(hashtable[k])
            res.append(arr[i])
           
        else:
            hashtable[arr[i]]=i
    
    if(sum(res)==x):
        return True
    return False
    
print(hasArrayTwoCandidates([1, 2, 4, 3, 6],5,10))