def firstElementKTime(a, n, k):
    ht={}
    for i in a:
        if (i not in ht):
            ht[i]=1
        
        else:
            ht[i]=ht[i]+1
            if(ht[i]==k):
                return i
    

print(firstElementKTime([1, 7, 7, 4, 4, 8, 7],7,2))