# 1차 코딩 - runtime error
import sys
N, M = map(int, sys.stdin.readline().split())

id_list = []
pw_list = []
for i in range(N):
    id, pw = map(str, sys.stdin.readline().split())
    id_list.append(id)
    pw_list.append(pw)

address = [sys.stdin.readline().strip() for _ in range(M)]
for i in address:
    idx = id_list.index(i)
    print(pw_list[idx]
 
 
# 2차 코딩 - 정답(11068ms)
import sys
N, M = map(int, sys.stdin.readline().split())
memo = dict()
for _ in range(N):
    site, pw = sys.stdin.readline().split()
    memo[site] = pw

for i in range(M):
    site = input()
    print(memo[site])
    
    
    
# 3차 코딩 - 정답(332ms)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    site, pw = input().split()
    memo[site] = pw

for i in range(M):
    site = input().strip()
    print(memo[site])
