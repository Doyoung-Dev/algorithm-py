from itertools import combinations

# 입력 처리
nums = input().split()
num1 = int(nums[0])
num2 = int(nums[1])

# 영학이가 가진 카드 제거
remaining_cards = [i for i in range(1, 11) for _ in range(2)]
remaining_cards.remove(num1)
remaining_cards.remove(num2)

# 영학이의 족보 계산
if num1 == num2:  # 땡
    younghak_score = 10 + num1
else:  # 끗
    younghak_score = (num1 + num2) % 10

# 상대방 카드 조합
opponent_combinations = list(combinations(remaining_cards, 2))

# 승리 횟수 계산
win_count = 0
for opp1, opp2 in opponent_combinations:
    if opp1 == opp2:  # 땡
        opponent_score = 10 + opp1
    else:  # 끗
        opponent_score = (opp1 + opp2) % 10

    # 영학이가 이기는 경우
    if younghak_score > opponent_score:
        win_count += 1

# 확률 계산
total_combinations = len(opponent_combinations)
win_probability = win_count / total_combinations

# 결과 출력 (소수점 셋째 자리까지)
print(f"{win_probability:.3f}")


# Try: 문제 이해 오류
# nums = input().split()
# num1 = int(nums[0])
# num2 = int(nums[1])
# k = num1+num2+1
#
# if num1==num2:
#     k = num1+1
# originList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if k > 10:
#     print(1.000)
# else:
#     taeng = (10-k+1)
#
#     listA = originList.copy()
#     listA.remove(num1)
#     listB = originList.copy()
#     listB.remove(num2)
#     sumList = listA+listB
#     sumList.sort()
#     sumList.reverse()
#     print(sumList)
#     sumList2 = sumList.copy()
#     test = []
#     gut = 0
#
#     tryList1 = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     tryList2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#     for i in range(k, 10, 1):
#         sumList = sumList2.copy()
#         for _ in range(18):
#             target = sumList.pop()
#             if tryList1[i]<=target: break
#             if tryList1[i]-target in sumList:
#                 gut += 1
#                 test.append([target, tryList1[i]-target])
#     for i in range(k, 10, 1):
#         sumList = sumList2.copy()
#         for _ in range(18):
#             target = sumList.pop()
#             if tryList2[i]<=target: break
#             if tryList2[i]-target in sumList:
#                 test.append([target, tryList2[i]-target])
#                 gut += 1
#
#     print(test)
#     print(taeng)
#     print(gut)
#     print((taeng+gut)/81/2)
#     # print(round((taeng+gut)/81), 3)
