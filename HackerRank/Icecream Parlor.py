#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

def icecreamParlor(m, arr):
    result = []
    for pair in combinations(arr, 2):
        print(f"pair: {pair}")
        if pair[0] + pair[1] == m:
            if pair[0] == pair[1]:
                result.append(arr.index(pair[0])+1)
                print(f"{arr.index(pair[0])+1}")
                arr.pop(arr.index(pair[0]))
                result.append(arr.index(pair[1])+2)
                print(f"{arr.index(pair[1])+2}")
            else:
                result.append(arr.index(pair[0])+1)
                print(f"{arr.index(pair[0])+1}")
                result.append(arr.index(pair[1])+1)
                print(f"{arr.index(pair[1])+1}")
    
    return result


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))

