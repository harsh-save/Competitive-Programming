import math
def searchRotated(arr,n,key):
    left=0
    right=n-1
    while(left<=right):
        middle=math.floor((left+right)/2)
        if(arr[middle]==key):
            return middle
        if(arr[left]<=arr[middle]):
            #left part is sorted
            if(key>arr[left] and key<arr[middle]):
                right=middle-1
            else:
                left=middle+1
        
        else:
            #right part is sorted
            if(key>arr[middle] and key<arr[right]):
                left=middle+1
            else:
                right=middle-1
    return -1

print(searchRotated([3, 5, 1, 2],4, 6))