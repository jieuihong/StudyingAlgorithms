n1, n2 = map(int, input().split())

def get_gcd(x, y):
    if x > y:
        while y:
            x, y = y, x%y
        return x
    else:
        while x:
            y, x = x, y%x
        return y

gcd = get_gcd(n1, n2)
print(gcd)
print(n1 * n2 // gcd)