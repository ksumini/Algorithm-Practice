# deque를 사용한 방법, 92ms
from collections import deque

N = int(input())
card = [i for i in range(1, N+1)]
queue = deque(card)

abandon = []
while len(queue) != 1: # 남는 카드가 1장일 때까지 while문 반복
    abandon.append(queue.popleft()) # pop(0)과 마찬가지로 가장 첫 번째 값 제거
    queue.append(queue.popleft())
abandon.extend(queue)
for i in abandon:
    print(i, end=' ')
    
    
# deque 사용 x 풀이, 76ms
N = int(input())
card = [i for i in range(1, N+1)]

abandon = []
for i in range(N-1): # N-1번 카드를 버리면 결국 한장의 카드가 남게됨
    abandon.append(card.pop(0))
    card.append(card.pop(0))
abandon.extend(card)
for _ in abandon:
    print(_, end=' ')
