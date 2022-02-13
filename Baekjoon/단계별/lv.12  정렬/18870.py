import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums_set = sorted(list(set(nums)))

nums_dict = {}
for i in range(len(nums_set)):
    nums_dict[nums_set[i]] = i

for num in nums:
    print(nums_dict[num], end=" ")
