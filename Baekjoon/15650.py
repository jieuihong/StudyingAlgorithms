import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().split()))

all_nums = []
for i in range(1, n+1):
    all_nums.append(i)
    
nums = list(combinations(all_nums, m))

for num in nums:
    print(' '.join(map(str, num)))
