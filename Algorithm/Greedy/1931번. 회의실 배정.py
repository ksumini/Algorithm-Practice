import sys
input = sys.stdin.readline

time = []
n = int(input())
for i in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda x: x[0]) # 시작 시간을 기준으로 오름차순 정렬
time = sorted(time, key=lambda x: x[1]) # 끝나는 시간을 기준으로 오름차순 정렬

cnt = 0
last = 0
for start, end in time:
    if start >= last:
        last = end
        cnt += 1
print(cnt)
