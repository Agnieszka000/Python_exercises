# HackerRank: Leap Year
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 ==0 and year % 400 == 0):
            return True
    return False

year = int(input())
print(is_leap(year))