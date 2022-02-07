# 1285번. 동전 뒤집기


# 먼저 열은 건드리지 않고 행만 뒤집는 모든 경우를 생각한다. 

# n = 3이라고 가정했을 때
# 모든 행을 바꾸지 않는 1가지
# 모든 행을 다 바꾸는 1가지
# 2개의 행을 골라 바꾸는 3가지
# 1개의 행을 골라 바꾸는 3가지

# 총 2^n의 경우의 수
# 비트 연산으로 표현하면 1 << n

# 0b0 -> 0 (모든 행을 바꾸지 않는 경우)
# 0b1 -> 1 (1개의 행을 바꾸는 경우)
# 0b10 -> 2 (1개의 행을 바꾸는 경우)
# 0b11 -> 3 (2개의 행을 바꾸는 경우)
# 0b100 -> 4 (1개의 행을 바꾸는 경우)
# 0b101 -> 5 (2개의 행을 바꾸는 경우)
# 0b110 -> 6 (2개의 행을 바꾸는 경우)
# 0b111 -> 7 (모든 행을 다 바꾸는 경우)

# 비트마스크 관련 참고 링크 : https://justkode.kr/algorithm/bitmash


n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n # 가능한 최대 뒷면의 갯수

# 행을 뒤집는 2^n의 경우의 수에 대해 모두 생각
for bit in range(1 << n): 
    tmp = [coin[i][:] for i in range(n)]
    for i in range(n):
        # i번째 수가 있나 없나 확인 할 때 (0이면 없고, 1 이상이면 있는 것)
        if bit & (1 << i): 
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'
              
    # 행을 뒤집는 경우를 완료한 후 열 기준으로 봤을 때 뒤집을지 말지를 결정        
    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tot += min(cnt, n-cnt)
    ans = min(ans, tot)

print(ans)
