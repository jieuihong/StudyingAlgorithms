def solution(progresses, speeds):
    remain = []
    for i in range(len(speeds)):
        q, r = divmod((100-progresses[i]), speeds[i])
        
        if r == 0:
            remain.append(q)
        else:
            remain.append(q+1)
            
    answer = []
    stack = []
    for i in range(len(remain)):
        if len(stack) == 0:
            stack.append(remain[i])
        elif remain[i] <= stack[0]:
            stack.append(remain[i])
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(remain[i])
            
    answer.append(len(stack))
    
    return answer
