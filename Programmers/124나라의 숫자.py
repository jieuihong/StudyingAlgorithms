def solution(n):
    answer = ''
    if n <= 3:
        answer += '124'[n-1]
    else:
        quo, rem = divmod(n-1, 3)
        answer += solution(quo) + '124'[rem]
        
    return answer
