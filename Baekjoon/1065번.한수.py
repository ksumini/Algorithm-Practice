N = int(input()) # N에 올 수 있는 자연수는 1부터 1000

cnt = 0
for i in range(1, N+1):
    if i <= 99: # 99보다 작을 때
        cnt+=1
    else: # 100 이상 1000 이하 일때 한 수 인지 확인
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            cnt +=1
print(cnt)
