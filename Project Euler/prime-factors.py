"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def prime_factors(n):
    factors = []
    #when n is even
    while n%2==0:
        factors.append(2)
        print(2)
        n=n/2
    
    for i in range(3,int(math.sqrt(n)+1),2):
        while i%i==0:
            factors.append(i)
            print(i)
            n=n/i
    
    if n>2:
        factors.append(n)
        print(n)
    return factors


print(prime_factors(13195))

        