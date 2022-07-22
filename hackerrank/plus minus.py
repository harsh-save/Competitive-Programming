from turtle import pos


def plusMinus(arr):
    positive=0
    negative=0
    zero=0
    size=len(arr)

    for i in range(len(arr)):
        
        if arr[i] >0:
            positive+=1
        elif arr[i]<0:
            negative+=1
        elif arr[i]==0:
            zero+=1
    
    print(f"{positive/size:.6f}")
    print(f"{negative/size:.6f}")
    print(f"{zero/size:.6f}")

plusMinus([-4, 3, -9, 0, 4, 1])  