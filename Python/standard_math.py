#Writing this library to make my life easier bc a lot of these problems require the same basic math functions
#NOTE: Not all functions are written entirely by me. I will modify efficient methods to fit my needs

import math


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

def num_divisors(n):
    end = math.sqrt(n)
    result = sum(2
		for i in range(1, int(end + 1))
		if n % i == 0)
    if end ** 2 == n:
        result -= 1
    return result

#method altered from stackoverflow to fit my needs
def binomial(x, y):
    if y == x:
        return (1)
    elif y == 1:
        return(x)
    elif y > x:
        return (0)
    else:  # will be executed only if y != 1 and y != x and x <= y
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x - y)  # that appears to be useful to get the correct result
        div = a // (b * c)
        return (div)

def num_to_word(n):
    ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]

    TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if(0 <= n < 20):
        return ONES[n]
    elif (20 <= n < 100):
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif(100 <= n < 1000):
        return ONES[n // 100] + "hundred" + (("and" + num_to_word(n % 100)) if (n % 100 != 0) else "")
    elif(1000 <= n < 1000000):
        return num_to_word(n // 1000) + "thousand" + (num_to_word(n % 1000) if (n % 1000 != 0) else "")
    else:
        print("Don't know how to fix at this point ")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
