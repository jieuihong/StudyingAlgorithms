import sys

n, m = list(map(int, sys.stdin.readline().split()))
nums = []


def dfs():
    if len(nums) == m:
        print(' '.join(map(str, nums)))

    else:
        for i in range(1, n + 1):
            if i not in nums:
                nums.append(i)
                dfs()
                nums.pop()


dfs()
