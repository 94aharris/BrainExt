#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#  https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
# 
# Outside the comments is what I did, but this is a better solution. Both these are O(N) time and O(N) space
#def whatFlavors(cost, money):
#    remains = dict()
#    for index, c in enumerate(cost):
#        if c not in remains:
#            remains[money - c] = index + 1
#        else:
#            print(remains[c], index + 1)

def populateMap(cost):
    i = 0
    costMap = {}
    while i < len(cost):
        if cost[i] in costMap:
            costMap[cost[i]].append(i)
        else:
            costMap[cost[i]] = [i]
        i += 1
    return costMap

def whatFlavors(cost, money):
    
    costMap = populateMap(cost)
    
    i = 0
    while i < len(cost):
        remain = money - cost[i]
        if remain in costMap:
            if len(costMap[remain]) > 1 :
                print(f"{costMap[remain][0]+1} {costMap[remain][1]+1}")
                return
            elif costMap[remain][0] != i :
                print(f"{i+1} {costMap[remain][0]+1}")
                return
        i += 1
    
    
        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
