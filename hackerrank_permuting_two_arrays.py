# Hackerrank, Challenge: Permuting Two Arrays

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'twoArrays' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B



def twoArrays(k, A, B):
    # Sort arrays A and B to facilitate the pairing logic
    A = sorted(A)
    B = sorted(B, reverse=True)
        
    # Try to find valid pairs where A[i] + B[i] >= k
    for digitA, digitB in zip(A, B):
        if digitA + digitB < k:
            return "NO"
    
    return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()