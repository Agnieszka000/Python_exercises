# www.hackerrank.com
# Challenge: Mini-Max Sum

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_items = sorted(arr)
    min_sum = int(sorted_items[0]) + int(sorted_items[1]) + int(sorted_items[2]) + int(sorted_items[3])
    max_sum = int(sorted_items[1]) + int(sorted_items[2]) + int(sorted_items[3]) + int(sorted_items[4])
    print(f"{min_sum} {max_sum}")

arr = [1,3,5,7,9]
miniMaxSum(arr)
