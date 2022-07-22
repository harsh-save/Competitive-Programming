def sum_of_primes(n):
    primes = []
    for i in range(1,n+1):
        for j in range(2,n):
            if n%i==0:
                primes.append(i)
    print(primes)
        

sum_of_primes(10)