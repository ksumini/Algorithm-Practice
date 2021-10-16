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
