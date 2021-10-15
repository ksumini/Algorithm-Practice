import sys
input = sys.stdin.readline

N = int(input())
employee = {}
for i in range(N):
    name, status = input().rstrip().split()
    if status == 'enter':
        employee[name] = status
    elif status == 'leave':
        del employee[name]

sorted(employee.keys(), reverse=True)

for j in sorted(employee.keys(), reverse=True):
    print(j)
