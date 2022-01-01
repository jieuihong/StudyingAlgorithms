import sys

inputs = []
for _ in range(10):
    inputs.append(int(sys.stdin.readline().rstrip()))

rem = []
for i in inputs:
    rem.append(i % 42)

rem_set = set(rem)

print(len(rem_set))
