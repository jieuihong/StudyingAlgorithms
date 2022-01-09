#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p, n, z = 0, 0, 0
    for num in arr:
        if num < 0:
            n += 1
        elif num == 0:
            z += 1
        else:
            p += 1
    r1 = "{:.6f}".format(p/(p+n+z))
    r2 = "{:.6f}".format(n/(p+n+z))
    r3 = "{:.6f}".format(z/(p+n+z))
    
    return r1, r2, r3

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for i in plusMinus(arr):
        print(i)
