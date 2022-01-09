import sys

while True:
    a, b = map(int,sys.stdin.readline().rstrip().split())

    if (a, b) == (0, 0):
        break
    else:
        print(a + b)
