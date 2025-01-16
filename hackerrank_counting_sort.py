# Hackerrank - Challenge: Counting Sort

# Counting sort is a sorting method. You create an integer array whose index range covers the entire range of values in your array to sort. 
# Each time a value occurs in the original array, you increment the counter at that index. 
# At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

# Given a list of integers, count and return the number of times each value appears as an array of integers.
# The frequency array shoul contain max. 100 integers.

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # Create a list of size 100 multiplying the number of O's by 100
    frequency_list = [0] * 100 
        
    # Count occurrences of each number in the input array
    for num in arr:
        frequency_list[num] += 1
    print(frequency_list)

arr = [1,1,3,2,1]
# the frequency_array should be [0,3,1,1], which is 0x0, 3x1, 1x2, 1x3

countingSort(arr)