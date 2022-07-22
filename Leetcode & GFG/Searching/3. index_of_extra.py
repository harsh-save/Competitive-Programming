import math
def findExtra(a,b,n):
    target=sum(a)-sum(b)
    left=0
    right=n-1
    while left<=right:
        middle=math.floor((left+right)/2)
        if a[middle]==target:
            return middle
        
        if(a[middle]<target):
            left=middle+1
        else:
            right=middle-1
    return -1


print(findExtra([3,5,7,9,11,13],[3,5,7,11,13],6))
