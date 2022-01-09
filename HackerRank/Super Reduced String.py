#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        print(f"elif block. s: {s}")
        return s
    else:
        i = 0
        while i < len(s) - 1:
            print(f"i: {i}")
            print(f"s: {s}")

            if s[i] == s[i + 1]:
                if len(s) == 2:
                    return ''
                else:
                    print(f"s[:i] + s[i + 2:]: {s[:i] + s[i + 2:]}")
                    return superReducedString(s[:i] + s[i + 2:])
            i += 1

        return s


if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)
