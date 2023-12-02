a = int(input())
card = []
answer = []

for i in range(1, a+1):
    card.append(i)
    
while (len(card) != 0):
    answer.append(card.pop(0))
    if(len(card) != 0):
        card.append(card.pop(0))

print(*answer)