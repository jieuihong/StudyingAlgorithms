import sys

n = int(sys.stdin.readline())

cups = [0]
for _ in range(n):
    cups.append(int(sys.stdin.readline()))

results = [0, cups[1]]
if n > 1:
    results.append(cups[1] + cups[2])

for i in range(3, n+1):
    # i 안 마심
    # i 마심
        # i-1 마심
        # i-1 안 마심
    m = max(results[i-3]+cups[i-1]+cups[i], results[i-2]+cups[i], results[i-1])
    results.append(m)

print(results[n])