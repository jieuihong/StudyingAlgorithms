def solution(s, n):
    new = ''
    lower = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V' ,'W', 'X', 'Y', 'Z']
    
    for char in s:
        print(char)
        if char == " ":
            new += char
        else:
            if char in lower:
                idx = lower.index(char)
                if idx + n > 25:
                    idx = idx + n - 26
                else:
                    idx += n
                new += lower[idx]
                print("index: %d" %idx)
                print("value: %s" %char)
            else:
                idx = upper.index(char)
                if idx + n > 25:
                    idx = idx + n -26
                else:
                    idx += n
                new += upper[idx]
                print("index: %d" %idx)
                print("value: %s" %char)
            
    answer = new
    return answer

s = input()
n = int(input())
print(solution(s, n))
