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
