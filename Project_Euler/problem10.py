
# The sum of the primes below 10 is 2+3+5+7=17.
# Find the sum of all the primes not greater than given .

# Input Format
# The first line contains an integer T i.e. number of the test cases.
# The next T lines will contains an integer N.

# Constraints
# 1 <= T <= 10^4
# 1 <= N <= 10^6

# Output Format
# Print the value corresponding to each test case in separate line.



import time


def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    prime2 = []
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    # return all prime numbers
    for p in range(2, n):
        if prime[p]:
            prime2.append(p)
    return(prime)

def sum_of_primes(p):
    summation = [0] * len(p)
    summation[0] = summation[1] = 0
    summation[2] = 2
    #return(summation)
    for i in range(3, len(summation)):
        if p[i] is True:
            summation[i] = summation[i-1] + i
        else:
            summation[i] = summation[i-1]
    return(summation)


start_time = time.clock()

primes = SieveOfEratosthenes(1000000)
s = sum_of_primes(primes)

# test cases

print(s[5])
print(s[10])
print(s[100])
print(s[34536])

print(time.clock() - start_time, "seconds")
