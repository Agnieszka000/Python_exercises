# HackerRank Challenge: Flipping bits
#
# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer. 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    # Flip the bits using bitwise NOT (~)
    flipped = ~n
    # Mask the flipped result to ensure it's treated as an unsigned 32-bit integer
    # We need it because Python treats binaries as signed numbers
    # Masking to 32 bits in binary - evry bit goint through "1" in mask stays unchanged.
    flipped_unsigned = flipped & 0b11111111111111111111111111111111
    return flipped_unsigned
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

