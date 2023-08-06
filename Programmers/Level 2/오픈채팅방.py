def solution(record):
    answer = []
    dic = {}
    for i in record:
        tmp = i.split()
        if len(tmp) == 3:
            dic[tmp[1]] = tmp[2]

    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter':
            answer.append(f'{dic[tmp[1]]}님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(f'{dic[tmp[1]]}님이 나갔습니다.')
    
    
    return answer
