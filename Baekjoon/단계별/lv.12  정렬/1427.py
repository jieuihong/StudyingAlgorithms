import sys

nums = list(map(int, list(sys.stdin.readline().rstrip())))
nums.sort(reverse=True)

for n in nums:
    print(n, end='')
