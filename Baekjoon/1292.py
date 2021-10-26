import sys

nums = list(map(int, sys.stdin.readline().split()))
num1 = nums[0]
num2 = nums[1]

arr = [0]
for i in range(1, 46):
    arr += [i] * i

sum = 0
for i in range(num1, num2+1):
    sum += arr[i]
    
print(sum)
