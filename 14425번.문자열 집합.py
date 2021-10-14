# 1차 시도(4728ms)
N, M = map(int, input().split())
cnt = 0
S = [input() for i in range(N)]

for j in range(M):
    if input() in S:
        cnt += 1
print(cnt)



# 입력시간 비교: https://www.acmicpc.net/blog/view/56
# 같이 보면 좋은 기본적인 문제: https://www.acmicpc.net/problem/15552
# input() 같은 경우 입력 시간 느려서 runtime error 자주 발생
# sys.stdin.readline()은 input()보다 평균적으로 1/3밖에 안걸림

# 코드 수정(152ms)
import sys
input = sys.stdin.readline

count = 0
N, M = map(int, input().split())
strings = {sys.stdin.readline() for i in range(N)}
for j in range(M):
    a = input()
    if a in strings:
        count += 1
print(count)
