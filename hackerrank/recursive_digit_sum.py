def superDigit(n,k):
    p=str(n)*k
    sum_num=0
    for i in range(len(p)):
        sum_num+=int(p[i])
    
    if sum_num <10:
        return str(sum_num)
    else:
        return superDigit(sum_num,1)


print(superDigit(9875 ,4))