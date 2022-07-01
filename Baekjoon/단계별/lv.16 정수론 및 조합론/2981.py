from decimal import MIN_EMIN


n = int(input())

nums = [int(input()) for _ in range(n)]

equal_remainders = []
for i in min(nums):
    temp = nums[0] % i

    for j in range(1, n):
        if 