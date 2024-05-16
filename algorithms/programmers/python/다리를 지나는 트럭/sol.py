def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    
    bridge = deque([0]*bridge_length) # 다리
    time = 0 # 시간
    
    cnt_weight = 0
    while len(truck_weights) > 0:
        time += 1
        cnt_weight = cnt_weight - bridge.popleft()
        if cnt_weight + truck_weights[0] <= weight:
            cnt_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    time += bridge_length
    return time
