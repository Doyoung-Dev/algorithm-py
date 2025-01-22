import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
nums = list()


def bfs(x, y):
    queue = deque([(x, y)])
    matrix[x][y] = 0
    num = 1
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            if 0 <= cx + dx[k] < N and 0 <= cy + dy[k] < N and matrix[cx + dx[k]][cy + dy[k]] == 1:
                matrix[cx + dx[k]][cy + dy[k]] = 0
                queue.append((cx + dx[k], cy + dy[k]))
                num += 1
    return num


for i in range(N):
    line = input()
    for j in range(N):
        matrix[i][j] = int(line[j])

for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1:
            num_sums = bfs(a, b)
            nums.append(num_sums)
            cnt += 1

print(cnt)
nums.sort()
print("\n".join(map(str, nums)))
