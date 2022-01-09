import sys

n, x = map(int,sys.stdin.readline().rstrip().split())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

for i in lst:
    if i < x:
        print(i, end=' ')
