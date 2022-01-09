from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        print(i)
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())
for j in range(a, b + 1):
    if is_prime(j):
        print(j)
