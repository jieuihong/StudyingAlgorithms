import sys

n = int(sys.stdin.readline())

members = []
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    members.append((int(a), b))

members.sort(key=lambda key: key[0])

for m in members:
    print(m[0], m[1])
