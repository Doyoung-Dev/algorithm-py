# 1. input N, T_list, P_list
N = int(input())
T_list = list()
P_list = list()
sums = list()
for _ in range(N):
    t, p = map(int, input().split())
    T_list.append(t)
    P_list.append(p)

# # 2. N만큼 for문 돌면서 T의 경우의 수 뽑기, 이때 P값 같이 계산
# for start in range(N):
#     sum = 0
#     i = start
#     while i < N:
#         if T_list[i] + i - 1 < N:
#             sum += P_list[i]
#             i += T_list[i]
#         else:
#             i += 1
#     sums.append(sum)
# # 3. 최댓값의 P 출력
# print(max(sums))

# 2. x일이후 퇴사일까지 벌 수 있는 최대 이익을 저장하는 dp[] 생성
# 이때 dp 는 N+1 길이로 생성하고, 0으로 초기화
dp = [0] * (N+1)

# 3. N-1부터 0까지 돌면서 최대 이익을 구하여 dp 에 저장
for day in range(N-1, -1, -1):
    pay = P_list[day]
    time = T_list[day]
    if day+time <= N:
        dp[day] = max(pay + dp[day+time], dp[day+1])
    else:
        dp[day] = dp[day+1]

# 4. 1일 이후 퇴사일까지 벌 수 있는 최대 이익을 출력
print(dp[0])
