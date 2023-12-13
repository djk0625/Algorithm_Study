n = int(input())
i = 0
answer = 0

while True:
    if n > i:
        i += 1
        n = n-i
        answer += 1
    else:
        print(answer)
        break;