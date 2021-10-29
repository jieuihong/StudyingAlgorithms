from itertools import combinations

def solution(numbers):
    pairs = list(combinations(numbers, 2))
    
    answer = []
    for pair in pairs:
        summ = pair[0] + pair[1]
        if summ not in answer:
            answer.append(summ)
        
    answer.sort()
    return answer
