#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    am_pm = s[-2:]
    
    hms = s[:-2].split(':')
    if am_pm == "AM":
        if hms[0] == '12':
            h = '00'
        else:
            h = hms[0]
        m = hms[1]
        s = hms[2]
    else:
        if hms[0] == '12':
            h = '12'
        else:
            h = str(int(hms[0]) + 12)
        m = hms[1]
        s = hms[2]
    
    return f"{h}:{m}:{s}"
        

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
