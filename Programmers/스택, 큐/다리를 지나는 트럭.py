def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    on_bridge = []
    time = 0
    t_sum = 0
    
    if len(truck_weights) == 1:
        return bridge_length+1
    
    while len(truck_weights) > 0:
        time += 1
        
        if t_sum + truck_weights[-1] <= weight:
            t = truck_weights.pop()
            on_bridge.append((bridge_length, t))
            t_sum += t

        on_bridge = [(i-1, j) for (i, j) in on_bridge]
        
        for i in on_bridge:
            if i[0] == 0:
                t_sum -= i[1]
                on_bridge.remove(i)

        
    return time + bridge_length