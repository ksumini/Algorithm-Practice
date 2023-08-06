# 전화번호 뒷자리 네자리 수를 제외한 나머지 번호는 '*'로 표시
# 파이썬은 문자열 곱셈이 가능!

def solution(phone_number):
    answer = len(phone_number[:-4]) * '*' + phone_number[-4:]
    return answer
