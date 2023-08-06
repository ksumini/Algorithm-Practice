# 조합은 서로 다른 n개 중에 r개를 선택하는 경우의 수(순서 X)
# 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 구하는 문제이므로 itertools에서 조합(combinations) 함수 사용
from itertools import combinations
def solution(numbers):    
    combi = list(combinations(numbers, 2)) 
    ans = set() # 중복된 수 제거를 위해 set() 사용
    for number in combi:
        ans.add(sum(number))
    ans = sorted(list(ans)) # 리스트 타입으로 변환후 오름차순 정렬
    return ans

# 이중 for문을 사용한 풀이
def solution(numbers):
    ans = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ans.append(numbers[i] + numbers[j])
    return sorted(list(set(ans)))
