import sys
n = int(input())
a = sorted(list(map(int, sys.stdin.readline().split()))) # 오름차순으로 정렬
x = 1
for i in a: # 1부터 비교하면서 다르면 출력
    if i == x:
        x += 1
    else:
        break
print(x)
