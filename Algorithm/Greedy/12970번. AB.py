# 12970번. AB

# 매개변수 word를 가지는 함수 check를 정의한다.
# AB쌍의 수를 세기 위한 변수 cnt를 0으로 정의한다.
# word의 길이-1만큼 반복하는 i에 대한 for문을 돌린다.
# word[i]가 A일 경우,
# i+1부터 word의 길이-1까지 반복하는 j에 대한 for문을 돌린다.
# 만약 word[j]가 B일 경우 cnt를 1 증가시킨다.
# cnt를 반환한다.

# n만큼 반복하는 i에 대한 for문을 돌린다.
# s[i]를 A로 갱신한다.
# 만약 check(s)가 k와 같을 경우 반복문을 종료한다.
# 만약 check(s)가 k보다 클 경우 s[i]를 B로 갱신한다.

# 문자열 s는 'A'와 'B'로 이루어져 있다는 조건이 있기 때문에 한 가지 알파벳으로만 이루어진 경우 -1을 출력한다.


n , k = map(int,input().split())

# 'B'로 이루어진 문자열로 초기값 설정
s = 'B'*n
s = list(s)

def check(word):
    cnt = 0
    for i in range(len(word)-1):
        if word[i] == 'A':
            for j in range(i+1,len(word)):
                if word[j] == 'B':
                    cnt += 1
    return cnt
  
  
for i in range(n):
    s[i] = 'A'
    if check(s) == k:
        break
    elif check(s) > k:
        s[i] = 'B'

answer = "".join(s)

if answer=='B'*n or answer=='A'*n:
    print(-1)
else:
    print(answer)
