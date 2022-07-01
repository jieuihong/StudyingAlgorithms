def n_base(m, n):
    num  =  ''
    while m > 0:
        m, r = divmod(m, n)
        num += str(r)
    return num[::-1]

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        

def solution(n, k):
    new_num = n_base(n, k)
    
    primes = []
    l = len(new_num)
    for i in range(l-1):
        for j in range(i+1, l+1):
            temp = new_num[i:j]
            if is_prime(int(temp)) is True:                  
                if '0' not in temp:
                    if i == 0 and new_num[j] == '0':
                        primes.append(int(temp))
                    elif j == l and new_num[i-1] == '0':
                        primes.append(int(temp))
                    elif new_num[i-1] == '0' and new_num[j] == '0':
                        primes.append(int(temp))
    return len(primes)