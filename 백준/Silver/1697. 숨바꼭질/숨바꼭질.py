import queue
from collections import deque
from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

visited = [False] * 100001


def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True

    while queue:
        current, time = queue.popleft()

        if current == K:
            return time

        for next in(current - 1, current + 1, current * 2):
            if 0 <= next <= 100000 and not visited[next]:
                queue.append((next, time + 1))
                visited[next] = True


print(bfs(N))