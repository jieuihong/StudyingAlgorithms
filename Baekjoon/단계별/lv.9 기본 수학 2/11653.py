num = int(input())


def factorization(n):
    if n == 1:
        return
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"i: {i}, n: {n}\n")
                return factorization(n // i)
            else:
                pass


if __name__ == "__main__":
    factorization(num)
