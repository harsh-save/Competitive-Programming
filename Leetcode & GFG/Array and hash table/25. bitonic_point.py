def findMax(arr,n):
    prev =0
    for i in range(n):
        if(arr[i]>prev):
            prev = arr[i]
        
    return prev

print(findMax([1, 45, 47, 50, 5],5))