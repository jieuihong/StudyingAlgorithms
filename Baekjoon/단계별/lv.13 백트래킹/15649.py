import sys

n, m = list(map(int, sys.stdin.readline().split()))
nums = []


def dfs():
    print(f"nums: {nums}")
    if len(nums) == m:
        print(' '.join(map(str, nums)))

    else:
        for i in range(1, n + 1):
            if i not in nums:
                nums.append(i)
                print("append")
                dfs()
                nums.pop()
                print("popped")


dfs()
