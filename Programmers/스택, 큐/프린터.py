def solution(priorities, location):
    queue = []
    result = []
    
    for l, p in enumerate(priorities):
        queue.append((l, p))
    
    def will_print(queue, i):
        for q in queue:
            if i < q[1]:
                return False
        else:
            return True
        
    while len(queue) > 0:
        document = queue[0]
        
        if will_print(queue, document[1]):
            result.append(document)
            queue.remove(document)
        else:
            queue.append(document)
            queue.remove(document)
            
    for i in range(len(result)):
        if result[i][0] == location:
            return i+1