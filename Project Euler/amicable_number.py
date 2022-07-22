def factors(n):
    sum_fact=0
    for i in range(1,10):
        if n%i==0:
            sum_fact+=i


def amicable_number(n):
    sum__ami=0
    for i in range(10,1,-1):
        for j in range(1,10,1):
            if i%j==0:
                sum__ami+=j
        if (sum__ami==factors(sum__ami)):
            print(sum__ami,factors(sum__ami))
    




amicable_number(5)