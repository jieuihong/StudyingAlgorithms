import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

new = []
m = max(lst)
for i in lst:
    new.append(i/m*100)

print(sum(new)/n)
