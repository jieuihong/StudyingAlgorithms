from itertools import combinations

n, num = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))

combs = combinations(cards, 3)
closest = 0
for c in combs:
    if closest < sum(c) <= num:
        closest = sum(c)

print(closest)
