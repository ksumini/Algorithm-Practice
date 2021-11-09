def solution(s):
    length = []
    result = ""

    if len(s) == 1:  # 문자열의 길이가 1인 경우
        return 1
    for step in range(1, len(s)//2+1): # 문자를 자를 수 있는 최대 단위는 전체 길이의 절반
        cnt = 1
        tmp = s[:step]

        for i in range(step,len(s), step):
            if s[i:i+step] == tmp: # tmp에 저장해 둔 문자와 다음 문자가 같은 경우
                cnt += 1
            else: # 같은 문자가 아닌 경우
                if cnt == 1: 
                    cnt = "" 
                result += str(cnt) + tmp
                tmp = s[i:i+step] # 현재 문자를 tmp(기준문자)로 지정
                cnt = 1 # 다시 카운트는 1로 초기화
        if cnt == 1: 
            cnt = ""
        result += str(cnt) + tmp
        length.append(len(result))
        result = "" # 초기화
    return min(length)
