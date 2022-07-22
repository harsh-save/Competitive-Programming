def lonelyinteger(a):
    sum_unique = sum(set(a))
    sum_arr=sum(a)
    return sum_unique*2-sum_arr

       

print(lonelyinteger([1,2,3,4,3,2,1]))