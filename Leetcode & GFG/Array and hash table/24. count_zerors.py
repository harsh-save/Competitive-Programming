def countZeros(arr,n):
    count=0
    for i in range(n):
        if(arr[i] == 0):
            count+=1
    return count

print(countZeros([0, 0, 0, 0, 0],5))