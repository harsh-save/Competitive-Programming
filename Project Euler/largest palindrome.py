"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPallindrome(n):
    if (str(n)==str(n)[::-1]):
        return True
    return False


def largest():
    pal=[]
    for i in range(100,999,1):
        for j in range(100,999,1):
            if isPallindrome(i*j):
                pal.append(i*j)
    
    print(max(pal))

largest()