#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    mc = 0
    pc = 0
    p = n % len(s)
    i = 0
    while (i < n and i < len(s)) :
        if (s[i].lower() == "a") :
            mc += 1
            if (i < p) :
                pc += 1
        i += 1        
    
    tc = pc + (mc * math.floor(n / len(s)))
    
    return tc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
10
