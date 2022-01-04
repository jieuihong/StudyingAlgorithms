import math

a, b, c = map(int, input().rstrip().split())

if a >= c:
    print(1)
else:
    print(math.ceil((c-b) / (a-b)))
