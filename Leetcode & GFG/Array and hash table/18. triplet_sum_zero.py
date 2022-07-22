def findTriplets(arr, n):
    triplet=0
    temp=[]
    for i in range(n):
        for j in range(i+1,n-1):
            if(arr[j] and arr[j+1]):
                if(arr[i]+arr[j]+arr[j+1]==0):
                    temp.append([arr[i],arr[j],arr[j+1]])
                    triplet+=1
    
    print(triplet)
    print(temp)

findTriplets([0, -1, 2, -3, 1],5)


