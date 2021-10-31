# 자료 구조, 문자열, 스택
# 첫 번째 stack을 생각하지 않고 푼 방법(68ms)
import sys
input = sys.stdin.readline
T = int(input()) # 테스트 데이터 개수
for i in range(T):
    string = input().strip()
    while True:
        if '()' in string:
            string = string.replace('()', '')
        else:
            break
    if string == '':
        print('YES')
    else:
        print('NO')
        
# 두 번째 stack을 생각하고 푼 방법(68ms)
T = int(input()) # 테스트 데이터 개수
for _ in range(T):
    string = input()
    vps = 0
    for i in string:
        if i =='(':
            vps += 1
        elif i == ')':
            vps -= 1
        if vps < 0:
            print('NO')
            break
    if vps > 0:
        print('NO')
    elif vps == 0:
        print('YES')
