def multiply (arr, n) : 
    mid=int(n/2)
    return sum(arr[0:mid])*sum(arr[mid:])

print(multiply([1, 2],2))