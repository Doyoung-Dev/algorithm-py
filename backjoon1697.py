from collections import deque


def find_min_time(N, K):
    visited = [False] * 100001

    queue = deque([(N, 0)])
    visited[N] = True

    while queue:
        current, time = queue.popleft()

        if current == K:
            return time

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))


N, K = map(int, input().split())

print(find_min_time(N, K))

# from collections import deque
#
# N, K = map(int, input().split())
# cnt = 0
#
#
# def move(x):
#     global cnt
#     cnt = 1
#     if x == K:
#         return
#     queue = deque()
#     if x - 1 == K or x + 1 == K or 2 * x == K:
#         cnt += 1
#         return
#     else:
#         queue.append(x - 1)
#         queue.append(x + 1)
#         queue.append(x * 2)
#         cnt += 3
#
#         while queue:
#             now_x = queue.popleft()
#             if now_x - 1 == K or now_x + 1 == K or 2 * now_x == K:
#                 cnt += 1
#                 return
#             else:
#                 cnt += 3
#                 for i in range(3):
#                     if i == 0:
#                         queue.append(now_x - 1)
#                     if i == 1:
#                         queue.append(now_x + 1)
#                     if i == 2:
#                         queue.append(now_x * 2)
#
#
# def get_answer(count):
#     answer = 0
#     while count > 0:
#         count -= pow(3, answer)
#         if count > 0:
#             answer += 1
#     return answer
#
#
# move(N)
# print(get_answer(cnt))
