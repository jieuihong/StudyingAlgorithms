#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    dist = []
    for i in range(n):
        if i in c:
            dist.append(0)
        else:
            shortest = n
            for s in c:
                if abs(s-i) < shortest:
                    shortest = abs(s - i)
            dist.append(shortest)
            
    return max(dist)
            
            
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)
