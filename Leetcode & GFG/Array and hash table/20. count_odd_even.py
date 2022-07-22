def countOddEven(arr, n):
    odd_count=0
    even_count=0
    for i in arr:
        if(i%2==1):
            odd_count+=1
        else:
            even_count+=1
    print("{} {}".format(odd_count,even_count))

print(countOddEven([1,2,3,4,5],5))
