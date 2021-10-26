import sys

num_input = int(sys.stdin.readline())

def get_gcd(a, b):
    if a > b:
        while b:
            a, b = b, a%b
        return a
    else:
        while a:
            b, a = a, b%a
        return b
    
for i in range(num_input):
    # get one input at a time
    num = list(map(int, sys.stdin.readline().split()))
    
    # get gcd & lcm
    gcd = get_gcd(num[0], num[1])
    lcm = (num[0] * num[1]) // gcd
    
    # print result
    print(lcm, gcd)
    
