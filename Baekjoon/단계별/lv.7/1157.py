word = input().upper()

d = {}

for c in word:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

sorted_d = sorted(d, key=d.get, reverse=True)

most = []
for i in range(len(sorted_d)):
    if d[sorted_d[i]] == d[sorted_d[0]]:
        most.append(sorted_d[i])

if len(most) > 1:
    print('?')
else:
    print(most[0])


print(f"word: {word}")
print(f"d: {d}")
print(f"sorted_d: {sorted_d}")
print(f"most: {most}")
