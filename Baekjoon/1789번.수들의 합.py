# 88ms
S = int(input()) 

sum_s = 0
num = 0

# 숫자의 합이 S를 처음으로 초과할 경우 현재까지 더한 자연수의 갯수에서 -1 
while sum_s <= S: 
    num += 1
    sum_s += num
print(num-1)
