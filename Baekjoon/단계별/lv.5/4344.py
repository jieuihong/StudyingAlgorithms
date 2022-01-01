import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    num = lst.pop(0)
    avg = sum(lst)/len(lst)

    smart = []
    for i in lst:
        if i > avg:
            smart.append(i)

    print(f"{len(smart) / num * 100:.3f}%")
