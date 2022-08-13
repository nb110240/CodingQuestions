#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'merge' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def merge(nums1, nums2):
    # Write your code here
    l = []
    for i in range(len(nums1)):
        l.append(nums1[i])
    for j in range(len(nums2)):
        l.append(nums2[j])
    return(sorted(l))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums1_count = int(input().strip())

    nums1 = []

    for _ in range(nums1_count):
        nums1_item = int(input().strip())
        nums1.append(nums1_item)

    nums2_count = int(input().strip())

    nums2 = []

    for _ in range(nums2_count):
        nums2_item = int(input().strip())
        nums2.append(nums2_item)

    result = merge(nums1, nums2)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()