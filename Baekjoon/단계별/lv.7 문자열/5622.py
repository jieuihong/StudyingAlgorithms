import sys

word = sys.stdin.readline().rstrip()
time = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for char in word:
    for d in dial:
        if char in d:
            time += (dial.index(d) + 3)

print(time)
