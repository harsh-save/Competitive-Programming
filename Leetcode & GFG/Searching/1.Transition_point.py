import math
def transitionPoint(arr,n):
    leftpointer=0
    rightpointer=n-1
    while leftpointer<=rightpointer:
        middle=math.floor((leftpointer+rightpointer)/2)
        if(arr[middle]==1 and arr[middle-1]==0): return middle
        if(arr[middle]==1 and arr[middle-1]!=0):
            leftpointer=middle-1
        if(arr[middle]==0): 
            leftpointer=middle+1
        
    return -1

print(transitionPoint([0,0,0,0,1,1,1,1,1,1],10))