"""
어떤 수열 A가 있을 때, K의 상한과 하한
- 상한: 크거나 같은 수 (큰 수 중 첫 번째 수)
- 하한: 작거나 같은 수 (크거나 같은 수 중 첫 번째 수)
- K의 개수: 상한의 위치 - 하한의 위치
-> K가 수열에 없으면 상한 == 하한

백준 문제: https://www.acmicpc.net/problem/10816
"""

# binary search
def binary_search(a, target, left, right):
    while left <= right:
        mid = (left+right)//2
        # 찾은 경우 중간점 인덱스 반환
        if a[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif a[mid] > target:
            right = mid-1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            left = mid+1
   return None


# lower bound
def lower_bound(a, target, left, right):
    while left <= right:
        mid = (left+right)//2
        if a[mid] == target:
            ans = mid
            right = mid-1
        elif a[mid] > target:
            right = mid-1
        else:
            left = mid+1

            
# upper bound
def upper_bound(a, target, left, right):
    while left <= right:
        mid = (left+right)//2
        if a[mid] == target:
            ans = mid+1
            left = mid+1
        elif a[mid] > target:
            right = mid-1
        else:
            left = mid+1
