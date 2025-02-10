# n, a, b = map(int, input().split())
# a_list = list(map(int, input().split()))  # 2x1 타일
# b_list = list(map(int, input().split()))   # 2x2 타일
# m = 0
# curr = 0
#
# a_list.sort(reverse=True)
# b_list.sort(reverse=True)
# i = 0
# j = 0
#
# while curr < n:
#     if curr == n-1:
#         m += a_list[i]
#         curr += 1
#         i += 1
#     elif j > b - 1 or i + 1 < a and a_list[i] + a_list[i+1] >= b_list[j]:
#         m += a_list[i] + a_list[i+1]
#         curr += 2
#         i += 2
#     else:
#         m += b_list[j]
#         curr += 2
#         j += 1
#
# print(m)

n, a, b = map(int, input().split())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))
m = 0

if n % 2 == 1:
    m += a_list[-1]
    a_list.pop(-1)
    n -= 1

for _ in range(0, n, 2):
    t1, t2 = 0, 0
    if len(a_list) >= 2:
        t1 = a_list[-1] + a_list[-2]
    if len(b_list) >= 1:
        t2 = b_list[-1]

    if t1 > t2:
        m += t1
        a_list.pop()
        a_list.pop()
    else:
        m += t2
        b_list.pop()

print(m)
