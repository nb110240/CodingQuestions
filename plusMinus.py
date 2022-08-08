#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg , zer = 0,0,0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos +=1
        elif arr[i] == 0:
            zer +=1
        else:
            neg +=1
    total = pos +neg + zer
    print(pos/total)
    print(neg/total)
    print(zer/total)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)