# 92ms
s = input()
stack = []
cnt = 0
for i in range(0, len(s)):
  if s[i] == '(':
    stack.append(i+1)
  else: # s[i] == ')'
    if stack[-1] == i : # 레이저
      stack.pop()
      cnt += len(stack)
    else: # 쇠막대기 끝
      stack.pop()
      cnt += 1
print(cnt)
