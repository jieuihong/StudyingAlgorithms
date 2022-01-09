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
    arr.sort()
    
    min = 0
    for i in range(4):
        min += arr[i]
    
    max = 0
    for j in range(1, 5):
        max += arr[j]

    return min, max
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(f"{miniMaxSum(arr)[0]} {miniMaxSum(arr)[1]}")
