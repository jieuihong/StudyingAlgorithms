import sys
import math

num_input = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))

def is_prime(num):
    prime = True
    
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                prime = False
            
    return prime

primes = 0
for i in range(num_input):
    prime = is_prime(inputs[i])
    
    if prime == True:
        primes += 1

print(primes)
