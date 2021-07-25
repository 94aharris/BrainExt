#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def parsePathStep(step):
    if (step.lower()) == 'd' : return -1
    elif(step.lower() == 'u') : return 1
    else : raise ValueError('Invalid Path Input')
        
    
def countingValleys(steps, path):
    
    takenSteps = 0
    altitude = 0
    inValley = False
    traversedValley = 0
    
    while (takenSteps < steps) :
        altitude += parsePathStep(path[takenSteps])
        takenSteps += 1
        if (altitude < 0) : inValley = True
        if (altitude == 0 and inValley) :
            traversedValley += 1
            inValley = False
    
    return traversedValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
