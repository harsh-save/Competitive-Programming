def duplicates( arr, n):
    hashtable={}
    for i in range(n):
        if arr[i] not in hashtable:
            hashtable[arr[i]]=1
        else:
            hashtable[arr[i]]=hashtable[arr[i]]+1
    
    
    res=[]
    for key,val in hashtable.items():
        if val>1:
            res.append(str(key))
    if(len(res)==0):
        return -1
      
    return res


print(duplicates([0,3,1,2,2,3,3],7))