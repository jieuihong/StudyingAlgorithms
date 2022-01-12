num = int(input())


def factorization(n):
    if n == 1:
        return
    else:
        for i in range(2, n+1):
            if n % i == 0:
                print(i)
                return factorization(n // i)
            else:
                pass


if __name__ == "__main__":
    factorization(num)
