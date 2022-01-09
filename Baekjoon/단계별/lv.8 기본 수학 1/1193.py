n = int(input())

s = 1
cnt = 1
while n > s:
    cnt += 1
    s += cnt

n -= (s-cnt)
if cnt % 2 == 0:
    a, b = 1, cnt
    while n > 1:
        a += 1
        b -= 1
        n -= 1
else:
    a, b = cnt, 1
    while n > 1:
        a -= 1
        b += 1
        n -= 1

print(f"{a}/{b}")
