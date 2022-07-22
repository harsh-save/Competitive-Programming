def getPairsCount(arr, n, k):
    hashtable={}
    count=0
    for i in range(n):
        diff=k-arr[i]
        if(hashtable[diff]):
            count+=hashtable[diff]
        elif(diff not in hashtable):
            hashtable[arr[i]]=1
    return count

print(getPairsCount([1,5,5,5,5,7],6,10))