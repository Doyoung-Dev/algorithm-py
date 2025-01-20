import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())
my_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    my_graph[u].append(v)
    my_graph[v].append(u)

count = 0  # 연결 노드의 수
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        dfs(my_graph, i, visited)
        count += 1  # dfs 한 번 끝날 때마다 count+1

print(count)
