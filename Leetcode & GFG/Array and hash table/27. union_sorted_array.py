import re


def unionSortedArray (a,b,n,m):
    temp=[]
    for i in range(n):
        temp.append(a[i])
    
    for i in range(len(b)):
        temp.append(b[i])
    
    result=set()
    for i in range(len(temp)):
        result.add(temp[i])
    return result
    
   

print(unionSortedArray([2, 2, 3, 4, 5],[1, 1, 2, 3, 4],5,5))

