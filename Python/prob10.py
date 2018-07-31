# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def main():
    max = 2000000
    ans = sum(prime_nums(1999999))
    return ans

def prime_nums(n):
    primes = []
    for i in range(n):
        if(is_prime(i)):
            primes.append(i)
    return primes


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(int(x))) + 1, 2):
            if x % i == 0:
                return False
        return True



print(main())

