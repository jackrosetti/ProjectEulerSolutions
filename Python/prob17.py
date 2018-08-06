# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
#

#We need to get the names for each number then in a loop add the length of them up
#Recursion would be nice but i think the array solution is better

import standard_math

def main():
    res = sum(len(standard_math.num_to_word(i))for i in range(1, 1001))
    return str(res)

print(main())