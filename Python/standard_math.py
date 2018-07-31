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