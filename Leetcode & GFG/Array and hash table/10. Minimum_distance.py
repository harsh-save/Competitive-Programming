def minDistance(arr,n,x,y):
    if (x not in arr):
        return -1
    if (y not in arr):
        return -1
   
    
    x_pos=-1
    y_pos=-1

    for i in arr:
        if i==x:
            x_pos=i
        elif i==y:
            y_pos=i
    
    return abs(x_pos-y_pos)

print(minDistance([86,39,90,67,84,66,62],7,1,2))
