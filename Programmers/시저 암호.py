# 소문자와 대문자 확인
# isupper(), islower() 사용
# z 이후 값들은 알파벳 총길이(26)으로 나누었을때 나머지로 해결

def solution(s, n):    
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    
    for i in s:
        if i == ' ':
            ans += ' '
        elif i.isupper():
            end = alpha_upper.find(i) + n
            ans += alpha_upper[end % 26]
        elif i.islower():
            end = alpha_lower.find(i) + n
            ans += alpha_lower[end % 26]
    return ans


# 아스키 코드를 활용한 풀이
# ord(문자): 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
# chr(정수): 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환

def solution(s, n): 
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(ord('A') + (ord(s[i]) - ord('A') + n) % 26) # 대문자 'A'를 기준으로 n만큼 이동한 후 해당하는 알파벳 찾기
        elif s[i].islower():
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + n) % 26) # 소문자 'a'를 기준으로 n만큼 이동한 후 해당하는 알파벳 

    print("".join(s))
