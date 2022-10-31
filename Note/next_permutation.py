"""
다음 순열
1. A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다. (i는 맨 뒤 index부터) -> 즉, 순열의 마지막 수에서 끝나는 가장 긴 감소수열을 찾아야 한다.
2. j >= i이면서 A[j] > A[i-1]를 만족하는 가장 큰 j를 찾는다.
3. A[i-1]과 A[j]를 swap한다.
4. A[i]부터 순열을 뒤집는다.

- 다음 순열을 구하는 시간복잡도: O(N)
- 전체 순열을 모두 구하는 시간복잡도: O(N! * N) <-크기가 N인 수열의 서로 다른 순열은 총 N!개
"""

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0: # 마지막 순열
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True
