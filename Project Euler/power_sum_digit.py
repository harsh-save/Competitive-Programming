"""
215^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def power_sum_digits(n,pow):
    number=str(n**pow)
    sum=0
    for i in number:
        sum+=int(i)
    print(sum)

power_sum_digits(2,1000)