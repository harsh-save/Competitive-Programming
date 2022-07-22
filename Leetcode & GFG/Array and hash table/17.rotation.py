def findKRotation(arr,n):
    rightpointer=n-1
    rotate=0
    mid=int(n/2)
    for leftpointer in range(mid):
        if(arr[rightpointer]<arr[leftpointer]):
            rotate+=1
        rightpointer-=1
    
    return rotate

print(findKRotation([1, 2, 3, 4, 5],5))