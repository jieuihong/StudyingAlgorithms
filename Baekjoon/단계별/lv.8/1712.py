a, b, c = map(int, input().rstrip().split())

if c - b <= 0:
    print(-1)
else:
    print(a//(c-b) + 1)
