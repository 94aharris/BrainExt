#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numswaps = 0
    i = 0
    while (i < len(a)) :
        j = 0
        jswap = 0
        while (j<(len(a)-1)) :
            if (a[j] > a[j+1]) :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numswaps += 1
                jswap += 1
            j += 1
        if (jswap == 0) :
            break
        else :
            i += 1
    print (f"Array is sorted in {numswaps} swaps.")
    print (f"First Element: {a[0]}")
    print (f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
