x = {}
y = {}

for _ in range(3):
    c = input().rstrip().split()
    if c[0] in x:
        x[c[0]] += 1
    else:
        x[c[0]] = 1

    if c[1] in y:
        y[c[1]] += 1
    else:
        y[c[1]] = 1

answer = [0, 0]
for i in x:
    if x[i] == 1:
        answer[0] = i
for j in y:
    if y[j] == 1:
        answer[1] = j

print(" ".join(answer))