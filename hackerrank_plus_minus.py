# www.hackerrank.com
# Challenge: Plus Minus

import math
import os
import random
import re
import sys

arr = [-4,3,-9,0,4,1]
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pluses = []
    minuses = []
    zeroes = []

    for i in arr:
        if i < 0:
            minuses.append(i)
        elif i==0:
            zeroes.append(i)
        elif i>0:
            pluses.append(i)
    
    x = (len(pluses))/n
    print(f"{x:.6f}")

    y = (len(minuses))/n
    print(f"{y:.6f}")

    z = (len(zeroes))/n
    print(f"{z:.6f}")



n = int(6)
arr = [-4,3,-9,0,4,1]
plusMinus(arr)
