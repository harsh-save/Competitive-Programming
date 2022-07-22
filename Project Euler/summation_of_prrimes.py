"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_of_primes():
    primes = []
    for i in range(10,1,-1):
        for j in range(1,10,1):
            if i%j==0:
                primes.append(i)
    print(primes)

sum_of_primes()