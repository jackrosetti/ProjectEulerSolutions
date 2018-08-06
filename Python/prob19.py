# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Already did this in APCSP using Python's date library
# Brute force this thing lol
# You can tell this was written when i was a beginner because of how for out the code goes lol

import datetime

def main():
    ans = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if datetime.date(y, m, 1).weekday() == 6:
                ans += 1
    return str(ans)

print(main())