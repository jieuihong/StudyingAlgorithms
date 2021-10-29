def ternary_flipped(num):
    result = ''
    while num > 0:
        num, remainder = divmod(num, 3)
        result += str(remainder)
    return result

def solution(n):
    answer = int(ternary(n), 3)
    return answer
