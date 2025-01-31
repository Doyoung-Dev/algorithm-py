# N (1 ≤ N ≤ 1,500,000)
# (1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000)
import sys
input = sys.stdin.readline

n = int(input())
t = list()
p = list()
dp = [0] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for day in range(n - 1, -1, -1):
    time = t[day]
    pay = p[day]
    if day + time <= n:
        dp[day] = max(dp[day + time] + pay, dp[day + 1])
    else:
        dp[day] = dp[day + 1]
print(dp[0])
