score = []
for i in range(8):
    score.append(int(input()))
arr = sorted(score, reverse=True)
answer = []

for i in arr[:5]:
    answer.append(score.index(i)+1)

print(sum(arr[0:5]))
answer.sort()
print(*answer)