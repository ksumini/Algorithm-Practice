# 76ms
# 접근방법
# 입력된 줄의 첫 번째 숫자는 K
# 이후 입력된 숫자 K개는 S
# 서로 다른 수의 집합 S에서 순서에 상관없이 6개 선택(조합)

from itertools import combinations
K = 1
while K != 0:
    T = [i for i in map(int, input().split())]
    K = T[0]
    S = T[1:]
    if K != 0:
        for i in list(combinations(S, 6)):
            for j in i:
                print(j, end=' ')
            print()
        print()
