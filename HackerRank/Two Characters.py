#!/bin/python3

from itertools import combinations
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    
    if len(s) == 1:
        return 0
    
    unique = set(s)
    print(f"unique: {unique}")
    longest = 0
    
    for pair in combinations(unique, 2):
        matches = []
        for c in s:
            if c in pair:
                matches.append(c)
        print(f"matches: {matches}")
        if all(c1 != c2 for c1, c2 in zip(matches, matches[1:])):
            longest = max(longest, len(matches))
    
    return longest  

if __name__ == '__main__':
    l = int(input().strip())
    s = input()

    result = alternate(s)

    print(result)
