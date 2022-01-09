import sys

n = int(sys.stdin.readline())
new = n
cnt = 0

while True:
    a = new // 10
    b = new % 10
    c = (a + b) % 10

    new = (b * 10) + c

    cnt += 1
    
    if new == n:
        print(cnt)
        break

    
