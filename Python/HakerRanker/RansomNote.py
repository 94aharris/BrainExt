#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    d = {}
    for x in magazine :
        if x in d :
            d[x] += 1
        else :
            d[x] = 1
    
    for x in note :
        if x in d :
            if d[x] == 0 :
                print("No")
                return
            else :
                d[x] -= 1
        else :
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
