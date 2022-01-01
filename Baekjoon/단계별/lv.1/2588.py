import sys

n1 = int(sys.stdin.readline().rstrip())
n2 = sys.stdin.readline().rstrip()
a, b, c = map(int, (n2[0], n2[1], n2[2]))

print(n1 * c)
print(n1 * b)
print(n1 * a)
print(n1 * (c + b*10 + a*100))
