"""
어떤 수열 A가 있을 때, target의 상한과 하한
- 상한: 큰 수 중 첫 번째 수
- 하한: 크거나 같은 수 중 첫 번째 수
- target의 개수: 상한의 위치 - 하한의 위치
-> target이 수열에 없으면 상한 == 하한

백준 문제: https://www.acmicpc.net/problem/10816
"""
from bisect import bisect_left, bisect_right


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


# lower bound <- bisect_left(a, target)
def lower_bound(a, target, left, right): # left = 0, right = len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] >= target:
            right = mid
        else:
            left = mid+1
    return left

            
# upper bound <- bisect_right(a, target)
def upper_bound(a, target, left, right): # left = 0, right = len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] > target:
            right = mid
        else:
            left = mid+1
    return left
