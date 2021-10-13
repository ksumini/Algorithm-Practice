N, M = map(int, input().split())
cnt = 0
S = [input() for i in range(N)]

for j in range(M):
    if input() in S:
        cnt += 1
print(cnt)
