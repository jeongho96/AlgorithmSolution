import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (N + 1)


def dfs(start):
    visited[start] = 1
    print(start, end=" ")

    for visiting in range(1, N + 1):
        if graph[start][visiting] == 1 and visited[visiting] == 0:
            dfs(visiting)


visited_bfs = [0] * (N + 1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = 1

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for visiting in range(1, N + 1):
            if graph[current][visiting] == 1 and visited_bfs[visiting] == 0:
                visited_bfs[visiting] = 1
                queue.append(visiting)


dfs(V)
print()
bfs(V)
