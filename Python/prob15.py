# Starting in the top left corner of a 2×2 grid, and only being able to move to the
# right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#Thank god for Mr. Ray ingraining binomials into my head lol i thought i would need to use a
#2-D array and a handful of for loops. 

import standard_math

def main():
    return standard_math.binomial(40, 20)

print(main())