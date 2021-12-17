# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from
# 1 to N?
#
# Input Format
# First line contains T that denotes the number of test cases. This is followed by  lines, each containing an integer N.
#
# Constraints
# 1 <= T <= 10, 1 <= N <= 40
#
# Output Format
# Print the required answer for each test case.

import fractions

def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i)/fractions.gcd(ans, i)
    print(int(ans))


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lcm(n)