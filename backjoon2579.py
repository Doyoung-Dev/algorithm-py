n = int(input())
stair = [0]*301
dp = [0]*301

for i in range(1, n+1):
    stair[i] = int(input())

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])

for j in range(4, n+1):
    dp[j] = max(dp[j-3] + stair[j-1] + stair[j], dp[j-2] + stair[j])

print(dp[n])
