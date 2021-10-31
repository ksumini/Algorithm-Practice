import sys
input = sys.stdin.readline
K = int(input())
stack = []
# K의 개수만큼 정수 입력받음
for i in range(K):
    num = int(input())
    if num != 0: # 정수가 0이 아닌 경우
        stack.append(num)
    else: # 정수가 0인 경우
        stack.pop()
print(sum(stack))
