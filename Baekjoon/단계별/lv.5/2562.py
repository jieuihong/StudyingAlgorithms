import sys

lst = []
for i in range(9):
    n = int(sys.stdin.readline().rstrip())
    lst.append(n)

print(max(lst))
print(lst.index(max(lst))+1)
