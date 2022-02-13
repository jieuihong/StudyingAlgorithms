import sys

n = int(sys.stdin.readline())

coords = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coords.append((y, x))

coords.sort()
for c in coords:
    print(c[1], c[0])