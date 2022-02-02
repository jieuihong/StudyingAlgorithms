n = int(input())

nums = [0] * n
num_dict = {}
for i in range(n):
    num = int(input())
    nums[i] = num
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
nums.sort()

freq = 0
for j in num_dict:
    if num_dict[j] > freq:
        freq = num_dict[j]

cnt = 0
for k in num_dict:
    if num_dict[k] == freq:
        pass


print(round(sum(nums)/n))
print(nums[n//2+1])
print(freq)
print(max(nums) - min(nums))
