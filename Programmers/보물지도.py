def solution(n, arr1, arr2):
    bin1 = []
    bin2 = []
    for i in range(n):
        new1 = format(arr1[i], 'b')
        if len(new1) < n:
            diff = n - len(new1)
            new1 = ('0' * diff) + new1
        bin1.append(new1)
        print("new1 = %s" %new1)
        
        new2 = format(arr2[i], 'b')
        
        if len(new2) < n:
            diff = n - len(new2)
            new2 = ('0' * diff) + new2
        bin2.append(new2)
        print("new2 = %s" %new2)    
    secret_map = []
    for i in range(n):
        row = ''
        for j in range(n):
            if  bin1[i][j] == '0' and bin2[i][j] == '0':
                row += ' '
            else:
                row += '#'
        secret_map.append(row)
        print("row = %s" %row)
    
    return secret_map

print(solution(5, [0, 1, 2, 31, 3], [4, 5, 6, 30, 25]))
