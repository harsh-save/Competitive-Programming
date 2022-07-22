# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Note: Retun the index of Equilibrium point. (1-based index)

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 3 
# Explanation: For second test case 
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2).

def equilibriumPoint(A,N):
    total_sum=sum(A)
    left_sum=0
    right_sum=0
    for i in range(N):
        right_sum=total_sum-A[i]-left_sum
        if(left_sum==right_sum):
            return i+1
        left_sum+=A[i]

print(equilibriumPoint([1],1))