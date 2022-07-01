n = int(input())
nums = list(map(int, input().rstrip.split()))

asc = [1 for _ in range(n)]
desc = [1 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and asc[i] < asc[j]:
            asc[i] = asc[j] + 1

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if nums[i] > nums[j] and desc[i] < desc[j] + 1:
            desc[i] = desc [j] + 1
    
    result[i] = desc[i] + asc[i] -1

print(max(result))