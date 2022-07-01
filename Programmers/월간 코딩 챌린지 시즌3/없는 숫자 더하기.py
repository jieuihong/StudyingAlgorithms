def solution(numbers):
    tot = 0
    for i in range(10):
        if i not in numbers:
            tot += i
    return tot
