import math
def findFloor(A,N,X):
    left=0
    right=N-1
    while left<=right:
        middle=math.floor((left+right)/2)
        if(A[middle]<X):
            return middle
        if(A[middle]>X):
            right=middle-1
    return -1
print(findFloor([1,2,8,10,11,12,19],7,0))