def solution(record):
    users = {}
    lst_status = []
    for i in range(len(record)):
        # split string into lst (data)
        string = record[i]
        data = string.split()
        status = data[0]
        user_id = data[1]
        
        if status == "Leave":
            pass
        # 새로 들어왔든 이름을 바꿨든 어쨌든 user dict에 id: nickame 추가/변경
        else:
            users[data[1]] = data[2]
        
        lst_status.append([status, user_id])
        
    answer = []
    for stat in lst_status:
        if stat[0] == "Enter":
            answer.append(f"{users[stat[1]]}님이 들어왔습니다.")
        elif stat[0] == "Leave":
            answer.append(f"{users[stat[1]]}님이 나갔습니다.")
            
    return answer
