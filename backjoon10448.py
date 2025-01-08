triangle = [int(n*(n+1)/2) for n in range(1, 44, 1)]
eureka = [0] * 1001
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1
inputs = int(input())
for _ in range(inputs):
    print(eureka[int(input())])


# try 1 : 시간 초과
# inputs = int(input())
# for _ in range(inputs):
#     num = int(input())
#     if num == 3:
#         print(1)
#         continue
#     flag = False
#     for i in range(44, 0, -1):
#         if flag:
#             break
#         for j in range(i, 0, -1):
#             if flag:
#                 break
#             for k in range(j, 0, -1):
#                 if int(i * (i + 1) / 2) + int(j * (j + 1) / 2) + int(k * (k + 1) / 2) == num:
#                     print(1)
#                     flag = True
#                     break
#     if not flag:
#         print(0)
#
# try 2: 설계 부족
# listT = []
# for i in range(1, 44):
#     listT.append(int(i*(i+1)/2))
# inputs = int(input())
# for _ in range(inputs):
#     num = int(input())
#     temp = listT[:num-2]
#     for i in range(num-4, -1, -1):
#         for j in range(i, -1, -1):
#             for k in range(j, -1, -1):
#                 sum = temp[i]+temp[j]+temp[k]
#                 if sum == num:
#                     print(1)
#                     break
