import sys


n = int(sys.stdin.readline())
stack = []
answer = []
flag = 0
start = 1
    
for i in range(n):
    t = int(sys.stdin.readline())
    
    while start <= t:
        stack.append(start)
        answer.append("+")
        start += 1
    
    if stack[-1] == t:
        stack.pop()
        answer.append("-")
    
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)