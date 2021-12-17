# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
# a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

#Given N, Check if there exists any Pythagorean triplet for which a+b+c=N
#Find maximum possible value of abc  among all such Pythagorean triplets,
#If there is no such Pythagorean triplet print -1.

#Input Format
#The first line contains an integer T i.e. number of test cases.
#The next T lines will contain an integer N.

# Output Format
# Print the value corresponding to each test case in separate lines.



import math

#a^2 + b^2 = c^2 (1)
# a + b + c = N (2)
# sub 2 into 1 to find equation for a in terms of b and N.

def pythag(N):
    poss = [-1,]
    for b in range(2, (N // 3) + 1):
            a = (N**2 - 2*N*b)/(2*(N-b))
            if a % 1 == 0:
                c = N - a - b
                poss.append(int(a * b * c))
    return(max(poss))




print(pythag(2990))
print(pythag(2991))
print(pythag(2992))
print(pythag(2993))
print(pythag(2994))
print(pythag(2995))
print(pythag(2996))
print(pythag(2997))
print(pythag(2998))
print(pythag(2999))
print(pythag(3000))
