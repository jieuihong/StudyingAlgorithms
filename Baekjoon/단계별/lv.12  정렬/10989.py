import sys
MAX = 10000
n = int(sys.stdin.readline())

# count sort - 메모리 초과
#
# n = int(sys.stdin.readline())
#
# nums = []
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))
#
# l = len(nums)
#
# count = [0] * (MAX_NUM + 1)
# count_sum = [0] * (MAX_NUM + 1)
#
# for i in range(0, l):
#     count[nums[i]] += 1
#
# count_sum[0] = count[0]
# for i in range(1, MAX_NUM + 1):
#     count_sum[i] = count_sum[i - 1] + count[i]
#
# sorted_lst = [0] * (MAX_NUM + 1)
#
# for i in range(l - 1, -1, -1):
#     sorted_lst[count_sum[nums[i]]] = nums[i]
#     count_sum[nums[i]] -= 1
#
# for i in sorted_lst[:n]:
#     print(i)

#########################################################################

# nums = []
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))
#
# count = [0] * (MAX + 1)
#
# for num in nums:
#     count[num] += 1
#
# print(f"count: {count}")
#
# for i in range(MAX):
#     count[i+1] += count[i]
# print(f"count: {count}\n")
#
# sorted_lst = [-1] * n
# for i in nums:
#     sorted_lst[count[i]-1] = i
#     print(f"i: {i}, count[{i}]: {count[i]}")
#     print(f"sorted_lst: {sorted_lst}")
#     print()
#     count[i] -= 1
#
# for i in sorted_lst:
#     print(i)

#########################################################################

count = [0] * (MAX + 1)
for _ in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
