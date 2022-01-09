import sys

a, b = sys.stdin.readline().rstrip().split()

new_a = int(a[::-1])
new_b = int(b[::-1])

print(max(new_a, new_b))

