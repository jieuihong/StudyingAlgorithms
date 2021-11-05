def solution(s):
    min_length = len(s)

    for cut in range(1, int(len(s)/2)+1):
        temp_str = s[:cut]
        count = 1
        new_str = ''

        print(type(cut))
        for i in range(cut, len(s), cut):
            print(type(i))
            print(type(i+cut))
        
            
            if s[i:i+cut] == temp_str:
                count += 1
            else:
                if count == 1:
                    count = ''
                new_str += (str(count) + temp_str)
                temp_str = s[i:i+cut]
                count = 1
        
        temp_length = len(new_str)
        if temp_length < min_length:
            min_length = temp_length
        count = 1
        new_str = ''
    
    
    return min_length

print(solution('aabbcccdd'))
