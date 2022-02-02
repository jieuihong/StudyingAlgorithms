import sys

n = int(sys.stdin.readline())

ppl = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ppl.append((x, y))

for i in ppl:
    rank = 1
    for j in ppl:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

