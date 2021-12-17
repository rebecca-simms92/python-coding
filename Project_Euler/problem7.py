# By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13. 
# What is the Nth prime number?

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

# Constraints
# 1 <= T <= 10^3
# 1 <= N <= 10^4


# Output Format
# Print the required answer for each test case.

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


t = int(input().strip())
l = 0
i = 2 
d = []
for a0 in range(t):
    n = int(input().strip())
    while l < n:
        if(isPrime(i)):
            l += 1
            d.append(i)
        i += 1
    print(d[n-1])   


