# 자료 구조, 덱
# 108ms

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
item = list(map(int, input().split()))
number = deque([i+1 for i in range(N)])

# 1번 연산: deque.popleft()
# 2번 연산: dequqe.append(deque.popleft())
# 3번 연산: deque.appendleft(deque.pop())

cnt = 0
for _ in item:
    while True:
        # 찾는 원소값이 첫 번째 있는 경우
        if number.index(_) == 0:
            number.popleft() # 1번 연산
            break # 위치 N보다 위치 0과 더 가까운 경우
        elif number.index(_) - 0 <= len(number) - number.index(_): # 2번 연산
            number.append(number.popleft())
            cnt += 1
        else:
            number.appendleft(number.pop()) # 3번 연산
            cnt += 1
print(cnt)
