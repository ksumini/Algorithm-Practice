# 자료구조, 큐(76ms)
import sys
input = sys.stdin.readline
N = int(input())

queue = []
for i in range(N):
    order = input().split()
    if order[0] == 'push':
        queue.append(int(order[1]))
    if order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    if order[0] == 'size':
        print(len(queue))
    if order[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
