import math
def peakElement(arr, n):
    left=0
    right=n-1
    if(n==1):
        return 0
    while left <= right:
        middle=math.floor((left+right)/2)
        if(middle+1<n):
            left = middle+1
        else:
            return middle

print(peakElement([3,4],2))
