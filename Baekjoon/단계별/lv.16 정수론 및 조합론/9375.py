n = int(input())

for i in range(n):
    clothes = {}
    m = int(input())
    print(f"m: {m}")
    if m == 0:
        print(0)
    else:
        for j in range(m):
            o, c = input().split()
            if c in clothes:
                clothes[c] += 1
            else:
                clothes[c] = 1
        
        total = 1
        for k in clothes:
            total *= (clothes[k] + 1)

        print(total - 1)
    
    