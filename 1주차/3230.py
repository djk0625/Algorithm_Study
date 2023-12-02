a = int(input())

for i in range(a):
    n = list(map(int, input().split()))

    answer = sorted(n[1::], reverse=True)
    max_answer = max(answer)
    min_answer = min(answer)
    gap = answer[0] - answer[1]

    for k in range(2, len(answer)):
        gap = max(gap, answer[k-1] - answer[k])

    print(f'Class {i+1}')
    print(f'Max {max_answer}, Min {min_answer}, Largest gap {gap}')