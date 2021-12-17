# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + .. + 10^2 = 385. The square of the sum of the
# first ten natural numbers is, (1+2+..+10)^2 = 55^2 = 3025. Hence the absolute difference between the sum of the
# squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

# Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an
# integer, N.

# Output Format
# Print the required answer for each test case.

def diffsquares(n):
    square1 = (n*(n+1)*(2*n+1)//6)
    square2 = ((n*(n+1)//2)**2)
    diff = abs(square1 - square2)
    return(diff)


n1 = 3

n2 = 10

n3 = 5948350

print(diffsquares(n1))
print(diffsquares(n2))
print(diffsquares(n3))