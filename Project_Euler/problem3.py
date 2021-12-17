# The prime factors of 13195 are 5, 7, 13  and 29.
#
# What is the largest prime factor of a given number N?
#
# Input Format
# First line contains T, the number of test cases. This is followed by T lines each containing an integer N.
#
# Output Format
# For each test case, display the largest prime factor of N.

def prime_factors(n):
    p = 2
    while n >= p*p:
        if n % p == 0:
            n = n // p
        else:
            p += 1
    print(n)


n1 = 100

n2 = 10001

n3 = 1345629482

prime_factors(n1)
prime_factors(n2)
prime_factors(n3)


