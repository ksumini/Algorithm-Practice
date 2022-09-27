"""
어떤 수열 A가 있을 때, K의 상한과 하한
- 상한: 크거나 같은 수 (큰 수 중 첫 번째 수)
- 하한: 작거나 같은 수 (크거나 같은 수 중 첫 번째 수)
- K의 개수: 상한의 위치 - 하한의 위치
-> K가 수열에 없으면 상한 == 하한

백준 문제: https://www.acmicpc.net/problem/10816
"""

# lower bound
def lower_bound(a, left, right, target):
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
def upper_bound(a, left, right, target):
    while left <= right:
        mid = (left+right)//2
        if a[mid] == target:
            ans = mid+1
            left = mid+1
        elif a[mid] > target:
            right = mid-1
        else:
            left = mid+1
