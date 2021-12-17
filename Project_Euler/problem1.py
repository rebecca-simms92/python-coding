#Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below N.
#
# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an
# integer, N.
#
# Constraints
# 1 <= T <= 10^5, 1 <= N <= 10^9
#
# Output Format
# For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.


def sum(n, k):
    d = n // k
    return k * (d * (d + 1)) // 2


def euler1(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)


n1 = 1000000000

print(euler1(n1 - 1))  # below N

