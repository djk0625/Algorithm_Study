d, k = map(int, input().split())

dp = []
for i in range(d):
    dp.append(0)
 
dp[0], dp[1] = 1, 1

while True:
    for i in range(2, d):
        dp[i] = dp[i-1] + dp[i-2]
    
    if dp[d-1] == k:
        print(dp[0])
        print(dp[1])
        break
    
    elif dp[d-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    
    else:
        dp[1] += 1