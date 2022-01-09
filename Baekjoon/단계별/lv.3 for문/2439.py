import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    s = '*' * i
    print(s.rjust(n, ' '))
