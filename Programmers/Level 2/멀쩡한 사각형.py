import math
def solution(w,h):
    total = w * h # 원래 전체 사각형 수
    minus = w + h - math.gcd(w,h) # (가로 + 세로 - 두 수의 공약수)
    answer = total - minus
    return answer
