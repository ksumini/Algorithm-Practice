# 틀렸는데 왜 틀렸는지 모르겠.....
# 그리디알고리즘, 정렬

import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수 입력

for _ in range(T):
    N = int(input()) # 지원자의 수
    applicant = []
    for i in range(N):
        paper, interview = map(int, input().split()) # 서류심사 성적, 면접 성적의 순위
        applicant.append((paper, interview))

    applicant = sorted(applicant) # 서류점수 순위로 오름차순 정렬
    # 첫 번째 사람은 서류점수 순위 1등임으로 무조건 합격
    interview_cut = applicant[0][1] # 서류점수 순위 1등의 면접 순위

    cnt = 1
    for j in range(1, len(applicant)): # 서류점수 순위 1등의 면접 순위보다 높아야됨
        if applicant[j][1] < interview_cut:  # (서류1등보다) 면접 순위가 더 높은 지원자만 합격
            cnt += 1
            if applicant[j][1] == 1: # 면접순위 1등보다 서류점수 순위 낮은 지원자는 탈락
                break
    print(cnt)
