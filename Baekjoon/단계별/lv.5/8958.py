import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    ox = sys.stdin.readline().rstrip()
    
    score = 0
    c = 1
    for i in ox:
        if i == 'O':
            score += c
            c += 1
        else:
            c = 1

    print(score)
