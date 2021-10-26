# 68ms
import sys
input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split()))) # 시간을 오름차순으로 정렬했을 때 필요한 시간의 합의 최솟값이 됨

sum_time = 0
for i in range(len(P)):
    sum_time += sum(P[0:i+1]) # 정렬된 시간을 계속해서 더해주면서 합을 
print(sum_time)
