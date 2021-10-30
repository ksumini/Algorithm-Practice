# 구현, 자료 구조, 시뮬레이션, 덱, 큐
# 92ms
import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) ## 보드 크기
K = int(input()) ## 사과 개수


## NxN의 board를 만든다.
board = [[1]*(N+2)] + [[1]+[0]*N+[1] for _ in range(N)] + [[1]*(N+2)]

for i in range(K):
    row, col = map(int, input().split()) ## a,b:사과 위치
    board[row][col] = 2 ## 사과는 숫자 2로 표현

L = int(input()) ## 뱀의 방향 변환 횟수
change = []
## 뱀의 방향 변환 정보
for i in range(L):
    X, C = input().split()
    change.append([int(X), C])

time = 0 ## 첫 시작은 일단 0초부터
x,y = 1,1 ## 뱀의 첫 위치(1행 1열)
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} ## 0:상 1:우 2:하 3:좌

# 시계방향(D) : 상 - 우 - 하- 좌 - 상 순으로 바뀌고 (+1)
# 반시계방향(L) : 상 - 좌 - 하 - 우 - 상 순으로 바뀐다 (-1)
# 따라서 바뀌는 방향에 따라 +1, -1을 취한후 4로 나눈 나머지 값을 구하면 됨
    
d = 1 ## 현재 방향은 오른쪽 (동쪽)
snake = deque([[1,1]]) ## 뱀의 위치를 큐로 나타낸다.

## board -> 0:빈공간, 1: 벽, 2:사과, 3: 뱀
board[1][1] = 3 ## 처음 뱀이 (1,1)에 존재하므로

## 이동한 후에 뱀 머리의 위치가 벽이거나, 자신의 몸일 경우 stop
while True:
    ## 일단 뱀의 머리를 이동시킨다. 바라보고 있는 방향으로.
    x = x + direction[d][0]
    y = y + direction[d][1]
    
    ## 1) 이동한 곳에 사과가 있는 경우
    if board[x][y] == 2:
        board[x][y] = 3 # 사과 대신 뱀 머리
        snake.append([x, y]) # snake의 맨 오른쪽 원소: 머리, 맨 왼쪽 원소: 꼬리
        time += 1
    
    ## 2) 이동한 곳이 빈 공간인 경우
    elif board[x][y] == 0:
        board[x][y] = 3 # 뱀 머리 위치
        snake.append([x,y])
        del_x, del_y = snake.popleft() ## 뱀의 전체 길이는 변하지 않아야 하기 때문에 꼬리를 제거
        board[del_x][del_y] = 0
        time += 1
    
    ## 3) 나머지는 벽 또는 자신의 몸과 부딪힌 경우(게임 끝)
    else:
        time += 1
        break
    
        
    ## 뱀의 방향 전환 정보
    if len(change) != 0:
        if change[0][0] == time:
            if change[0][1] == 'L': ## 왼쪽으로 90도 회전
                d = (d-1)%4
            elif change[0][1] =='D': ## 오른쪽으로 90도 회전
                d = (d+1)%4
            del change[0] ## 방향 전환했으므로 제거

print(time)
