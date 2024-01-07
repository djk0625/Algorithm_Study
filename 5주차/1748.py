n = input()
t = len(n)

answer = 0

for i in range(1, t):
    answer += 9 * (10 ** (i-1)) * i

answer += ((int(n) - (10 ** (t-1))) + 1) * t

print(answer)