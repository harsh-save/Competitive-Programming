def remove_duplicate(A,N):
    pointer =0
    result=N
    for i in range(1,N):
        if(A[pointer]!=A[i]):
            pointer+=1
        else:
            result-=1
    return result

print(remove_duplicate([2, 2, 2, 2, 2],3))