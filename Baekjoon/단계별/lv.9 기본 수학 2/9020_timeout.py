from itertools import combinations


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


primes = []
for i in range(10000):
    if is_prime(i):
        primes.append(i)


for _ in range(int(input())):
    num = int(input())
    certain_primes = []
    ans = []
    for p in primes:
        if p > num:
            break
        else:
            certain_primes.append(p)
        if p + p == num:
            ans.append((p, p))

    combs = combinations(certain_primes, 2)
    for c in combs:
        if c[0] + c[1] == num:
            ans.append((c[0], c[1]))

    partition = ans[0]
    if len(ans) > 1:
        for a in ans:
            if a[1] - a[0] < partition[1] - partition[0]:
                partition = a
    print(partition[0], partition[1])






