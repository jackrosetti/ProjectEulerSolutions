# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

#start from 1,000,000 and do the sequence

def main():
    mode = 0
    j = 0
    while(j < 10 ** 6):
        res = chain(j)
        if (res > mode):
            mode = res
            value = j
        j += 1
    return value

def chain(n):
    results = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        results += 1
    return results

if __name__ == "__main__":
    print(main())