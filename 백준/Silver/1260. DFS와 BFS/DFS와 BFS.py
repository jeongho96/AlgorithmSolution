import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

# 그래프 초기화
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# DFS
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for node in range(1, N + 1):
        if graph[start][node] == 1 and not visited[node]:
            dfs(node)

# BFS
def bfs(start):
    queue = deque([start])
    visited_bfs = [False] * (N + 1)
    visited_bfs[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for node in range(1, N + 1):
            if graph[current][node] == 1 and not visited_bfs[node]:
                visited_bfs[node] = True
                queue.append(node)

# DFS 탐색
visited = [False] * (N + 1)
dfs(V)
print()

# BFS 탐색
bfs(V)
