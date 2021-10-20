# 572 ms
import sys
s = sys.stdin.readline().strip() # 문자열 입력 받기

ans = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1): 
        ans.append(s[i:j]) # 경우의 수 구하기
print(len(set(ans))) # 중복 제거후 개수
