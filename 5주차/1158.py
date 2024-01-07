N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = []
num = K - 1

for t in range(N):
    if len(arr) > num:
        answer.append(arr.pop(num))
        num += K - 1
    elif len(arr) <= num:
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += K - 1
    
print("<", ", ".join(str(i) for i in answer), ">", sep = '')