# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    ans = max(j * i
              for i in range (100, 1000)
              for j in range(100, 1000)
              if str(i * j) == str(i * j)[::-1])
    return ans

def is_palidrone(ans):
    if(ans < 10):
        return True
    if(str(ans[0]) != str(ans[-1])):
        return False
    return is_palidrone(str(ans[1 :: -1]))


if __name__ == "__main__":
    print(main())
