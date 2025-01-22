import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    matrix[x][y]= 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            if 0 <= cx + dx[i] < M and 0 <= cy + dy[i] < N and matrix[cx+dx[i]][cy+dy[i]] == 1:
                matrix[cx+dx[i]][cy+dy[i]] = 0
                queue.append((cx + dx[i], cy + dy[i]))



for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        i, j = map(int, input().split())
        matrix[i][j] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
