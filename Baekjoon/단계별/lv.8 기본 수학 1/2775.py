t = int(input())

ppl = [[i for i in range(1, 15)]]
for _ in range(14):
    lst = [1]
    lst.extend([0]*13)
    ppl.append(lst)

print(ppl)

for _ in range(t):
    fl = int(input())
    rm = int(input())

    for i in range(1, fl):
        print(ppl[i - 1])
        for j in range(1, 14):
            ppl[i][j] = sum(ppl[i-1][:j+1])

    for k in range(1, rm):
        print(f"ppl[{fl-1}][:{k}]: {ppl[fl-1][:k]}")
        ppl[fl][k] = sum(ppl[fl-1][:k+1])

    print(ppl)
    print(ppl[fl][rm-1])

