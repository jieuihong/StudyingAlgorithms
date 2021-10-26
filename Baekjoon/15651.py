import sys

n, m = list(map(int, sys.stdin.readline().split()))

result = []

def sol():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):  
            result.append(i)
            print(result)
            sol()
            result.pop()

sol()
