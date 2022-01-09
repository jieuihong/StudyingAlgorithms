#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):

    half_len = len(matrix)//2
    
    for i in range(len(matrix)):
        first_half, second_half = 0, 0
        for j in range(half_len):
            print(f"i, j = {i}, {j}")
            first_half += matrix[i][j]
            second_half += matrix[i][j + half_len]
            print(f"first half: {first_half}")
            print(f"second half: {second_half}")
        if first_half < second_half:
            matrix[i].reverse()
            print(f"reversed: {matrix[i]}")

    print(matrix)
    
    for i in range(len(matrix)):
        first_half, second_half = 0, 0
        for j in range(half_len):
            print(f"i, j = {i}, {j}")
            first_half += matrix[j][i]
            second_half += matrix[j + half_len][i]
            print(f"first half: {first_half}")
            print(f"second half: {second_half}")
        if first_half < second_half:
            matrix[i].reverse()
            print(f"reversed: {matrix[i]}")

    print(matrix)
    
    result = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            result += matrix[i][j]
    
    return result
            
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)
