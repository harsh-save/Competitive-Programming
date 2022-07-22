def missingNumber(arr,n):
    sum_of_n=int((n*(n+1))/2)
    return sum_of_n-sum(arr[0:n-1])


print(missingNumber([6,1,2,8,3,4,7,10,5],10))