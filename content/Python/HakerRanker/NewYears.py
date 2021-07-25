#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    i = 1
    tshift = 0
    for p in q :
        shift = p - i
        if (shift > 2) :
            print("Too chaotic")
            return
        for pr in q[max(p-2,0):i] :
            if pr > p :
                tshift += 1
        i += 1
    print(tshift)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
