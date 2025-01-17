import itertools
# 입력
N = int(input())

# 숫자 입력
nums = [i for i in map(int, input().split())]

# 연산자
operators_in = list(map(int, input().split()))
operators = []

for j in range(4):
    if j == 0:
        for _ in range(operators_in[j]):
            operators.append('+')
    if j == 1:
        for _ in range(operators_in[j]):
            operators.append('-')
    if j == 2:
        for _ in range(operators_in[j]):
            operators.append('*')
    if j == 3:
        for _ in range(operators_in[j]):
            operators.append('/')

comb = set(itertools.permutations(operators, N-1))
min_cal = float('inf')
# 최댓값이 음수인 경우가 있을 수 있으므로 초기화할때 float('-inf')
max_cal = float('-inf')

# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다
for cal in comb:
    calculated = nums[0]
    for c in range(N-1):
        if cal[c] == '+':
            calculated += nums[c+1]
        if cal[c] == '-':
            calculated -= nums[c+1]
        if cal[c] == '*':
            calculated *= nums[c+1]
        if cal[c] == '/':
            #  나눗셈은 정수 나눗셈으로 몫만 취한다
            # 음수를 양수로 나눌 때 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
            if calculated < 0:
                calculated = (abs(calculated) // nums[c+1]) * -1
            else:
                calculated = calculated // nums[c+1]
    max_cal = max(calculated, max_cal)
    min_cal = min(calculated, min_cal)
print(max_cal)
print(min_cal)
