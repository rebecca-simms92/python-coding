# A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit
# numbers is 101101 = 143 x 707.
#
# Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
#
# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an
# integer, N.
#
# Constraints
# 1 <= T <= 100, 101101<N<1000000
#
# Output Format
# Print the required answer for each test case in a new line.



def is_pali(x):
    num = str(x)
    return (num == num[::-1])



palindromeList = []
for i in range(100 ,1000):
    for j in range(100, 1000):
        i f(is_pali( i *j)):
            palindromeList.append( i *j)



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest = 0
    for i in palindromeList:
        if (i < n and i > largest):
            largest = i

    print(largest)



