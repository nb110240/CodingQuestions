#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. INTEGER badIndex
#

def maxIndex(steps, badIndex):
    # Write your code here
    i = 0
    t = 0
    for j in range(1,steps+1):
        #case1
        if i+j == badIndex:
            continue
        i += j 
    #case 2
    for k in range(2,steps+1):
        if k + t == badIndex:
            t = t

        t += k
    return max(i,t)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    badIndex = int(input().strip())

    result = maxIndex(steps, badIndex)

    fptr.write(str(result) + '\n')

    fptr.close()
