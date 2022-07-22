def pythagousTriplet(n):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            c=n-i-j
            if (i<j<c and i**2+j**2==c**2):
                print(i*j*c)

pythagousTriplet(1000)