import sys

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

count = {}
for num in set(nums):
    count[num] = nums.count(num)

print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
print(max(count, key=count.get))
print(max(nums)-min(nums))
