n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

cnt = 0
for c in coins:
    if c <= k:
        cnt += k // c
        k %= c

print(cnt)