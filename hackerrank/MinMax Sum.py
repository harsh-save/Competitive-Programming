def miniMaxSum(arr):
    sums=[]
    total_sum=0
    for i in range(len(arr)):
        total_sum+=arr[i]
    
    for i in range(len(arr)):
        temp=total_sum-arr[i]
        sums.append(temp)
    print("{} {}".format(min(sums),max(sums)))

miniMaxSum([1,3,5,7,9])
