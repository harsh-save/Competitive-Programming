from operator import le


def dia(n,arr):
    count_1=0
    count_2=0
    for i in range(len(arr)):
        count_1 +=arr[i][i]
        count_2+=arr[i][-1-i]
    return abs(count_1-count_2)


print(dia(3,[[1,2,3],[4,5,6],[9,8,9]]))