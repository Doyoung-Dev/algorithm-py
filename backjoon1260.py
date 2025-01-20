from collections import defaultdict

N, M, V = map(int, input().split())
my_graph = defaultdict(list)
graph2 = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    my_graph[u].append(v)
    my_graph[v].append(u)
    graph2[u].append(v)
    graph2[v].append(u)

print(my_graph)
# 그래프 정렬 (오름차순)
for key in my_graph:
    my_graph[key].sort()
print(my_graph)
print(graph2)

def dfs(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited


def bfs(graph, start_node):
    need_visit, visited = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit[0]
        del need_visit[0]

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


dfs_answer = dfs(my_graph, V)
bfs_answer = bfs(my_graph, V)

print(" ".join(map(str, dfs_answer)))
print(" ".join(map(str, bfs_answer)))
