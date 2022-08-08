#!/bin/python3

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
    min1 , max1 =0,0
    total = sum(arr)
    n = []
    for i in range(len(arr)):
        n.append(total - arr[i])
    min1 = min(n)
    max1 = max(n)
    print(min1,max1)

        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
