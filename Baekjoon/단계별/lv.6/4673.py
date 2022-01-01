def d(n):
    str_n = str(n)
    s = 0
    for c in str_n:
        s += int(c)

    return n + s

non_self = []

for i in range(10000):
    non_self.append(d(i))

non_set = set(non_self)

for j in range(10000):
    if j not in set(non_set):
        print(j)
