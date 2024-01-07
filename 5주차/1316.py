n = int(input())
answer = n

for i in range(n):
    t = input()

    for j in range(0, len(t)-1):
        if t[j] == t[j+1]:
            pass
        elif t[j] in t[j+1:]:
            answer -= 1
            break

print(answer)