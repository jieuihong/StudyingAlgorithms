import sys

n = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().rstrip().split()))

# dist = []
# 이중 for문이라 역시나 시간 초과
# for i in range(0, n):
#     tot = 0
#     for j in range(n):
#         tot += abs(houses[i] - houses[j])
#     dist.append(tot)
# print(houses[dist.index(min(dist))])

houses.sort()
print(houses[(n-1)//2])

