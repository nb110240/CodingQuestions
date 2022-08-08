#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    '''
    if it is 12pm return 12
    if it is 1pm return 13 
    if it is 2pm return 14
    
    '''
    new = s.split(':')
    no = 0
    res = []
    if new[2][2] == 'P' and new[0] != '12':
        no =(int(new[0])+12)
        new[0] = str(no)
    elif new[2][2] == 'A' and new[0] == '12':
        new[0] = '00'
    res.append(new[0])
    res.append(new[1])
    res.append(new[2][:2])
    return ':'.join(res)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
