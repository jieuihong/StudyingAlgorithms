import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(lst), max(lst))
