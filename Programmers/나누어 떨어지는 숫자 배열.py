def solution(arr, divisor):
    answer = []
    for i in arr:
        if not i % divisor:
            answer.append(i)
    if len(answer) == 0:
        return -1

    answer.sort()
    return answer
