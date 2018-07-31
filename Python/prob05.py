# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import fractions

def main():
    mult = 1
    for i in range(1, 21):
        mult *= i // fractions._gcd(i, mult)
    return mult

if __name__ == "__main__":
    print(main())