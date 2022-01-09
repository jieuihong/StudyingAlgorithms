x, y, w, h = map(int, input().rstrip().split())

print(min(x, y, w-x, h-y))
