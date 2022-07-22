def maxDays(arr, n):
    count=0
    while sum(arr)>0:
        arr=[x-1 for x in arr if x>0]
        count += 1
    return count

print(maxDays([1,1,2],4))