import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num, string = sys.stdin.readline().rstrip().split()
    ans = ''

    for c in string:
        ans += c*int(num)

    print(ans)
    
