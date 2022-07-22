def sum_square(n):
    sum1=int((n*(n+1)/2)**2)
    c=0
    for i in range(n+1):
        c+=i**2
    
    print(sum1-c)

    


sum_square(100)