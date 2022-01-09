from math import sqrt


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


primes = []
for j in range(2, 123456 * 2):
    if is_prime(j):
        primes.append(j)

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for p in primes:
        if n < p <= 2*n:
            cnt += 1
    print(cnt)
