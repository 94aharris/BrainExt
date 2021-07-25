
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    highest = 0
    r = 0
    while (r < (len(arr) -2)) :
        c = 0
        while (c < (len(arr[r]) -2)) :
            tsum = sum(arr[r][c:c+3]) + (arr[r+1][c+1]) + sum(arr[r+2][c:c+3])
            if (tsum > highest or (c == 0 and r == 0)) :
                highest = tsum
            c += 1
        r += 1
    return highest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
