def solution(id_list, report, k):
    reported = {}
    was_reported = {}
    
    for id in id_list:
        reported[id] = []
        was_reported[id] = 0
        
    for r in set(report):
        sub, obj = r.split()
        
        reported[sub].append(obj)
        was_reported[obj] += 1
        
    result = []      
    for r in reported:
        cnt = 0
        for p in reported[r]:
            if was_reported[p] >= k:
                cnt += 1
        result.append(cnt)
    
    return result