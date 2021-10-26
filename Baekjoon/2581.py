import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())


def is_prime(num):
    prime = True

    if num < 2:
        prime = False
    else:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                prime = False

    return prime

primes = []
for i in range(num1, num2+1):
    if is_prime(i) == True:
        primes.append(i)

prime_sum = sum(primes)
if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(primes[0])
