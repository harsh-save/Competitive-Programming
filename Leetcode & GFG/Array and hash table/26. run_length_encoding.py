def enccode(arr):
    arr=list(arr)
    count=1
    result=''
    for i in range(len(arr)):
        if(i+1<len(arr)):
            if(arr[i]==arr[i+1]):
                count+=1
            else:
                result+=arr[i]+str(count)
                count=1
    result+=arr[i]+str(count)
    return result

    

print(enccode('wwwwaaadexxxxxx'))



