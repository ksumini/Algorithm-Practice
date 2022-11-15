"""
<에라토스테네스의 체>
여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘 (+ N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.)

1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다.)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

시간복잡도: O(NloglogN)
단점: 메모리가 많이 필요하다(알고리즘을 수행할 때 N의 크기만큼 리스트를 할당해야 하기 때문)

Reference: https://www.youtube.com/watch?v=9rLFFKmKzno
"""

n = int(input())
arr = [True] * (n+1) # 처음엔 모든 수가 True인 것으로 초기화(0과 1은 제외)
arr[0] = arr[1] = False

# 에라토스테네스의 체
for i in range(2, int(n**(1/2))+1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if arr[i]: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

# 모든 소수 출력
prime_number = [i for i in range(len(arr)) if arr[i]]
print(prime_number)
