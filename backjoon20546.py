# 1. 입력
cash = int(input())
price = list(map(int, input().split()))

# 2. 준현, 성민 각각 계산
j_stock = 0
j_cash = cash
s_stock = 0
s_cash = cash

# 2-1. 준현 계산
for i in range(14):
    # 전량 매수
    num = j_cash // price[i]
    j_cash -= num * price[i]
    j_stock += num

# 2-2. 성민 계산
for j in range(3, 14, 1):
    # 3일 연속 하락
    if price[j-3] > price[j-2] > price[j-1]:
        # 전량 매수
        num = s_cash // price[j]
        s_stock += num
        s_cash -= num * price[j]
    # 3일 연속 상승
    if price[j-3] < price[j-2] < price[j-1]:
        # 전량 매도
        s_cash += s_stock * price[j]
        s_stock = 0


# for i in range(12):
#     if price[i] > price[i + 1] > price[i + 2] and i < 11:
#         # 전량 매도
#         s_cash = s_stock * price[i + 3]
#         s_stock = 0
#     if price[i] < price[i + 1] < price[i + 2] and i < 11:
#         # 전량 매수
#         num = s_cash % price[i + 3]
#         s_cash -= num * price[i + 3]
#         s_stock += num
# 3. 비교
j = j_cash + (j_stock * price[13])
s = s_cash + (s_stock * price[13])

if j > s:
    print("BNP")
elif j < s:
    print("TIMING")
else:
    print("SAMESAME")
