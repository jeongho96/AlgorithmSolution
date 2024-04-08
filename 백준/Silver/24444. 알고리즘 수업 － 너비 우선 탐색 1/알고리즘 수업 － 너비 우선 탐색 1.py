from sys import stdin
from collections import deque

input = stdin.readline

# 노드 수, 간선 수, 시작 노드 번호 입력
node, voltex, start = map(int, input().rstrip().split())

# 그래프 초기화
graph = [[] for _ in range(node + 1)]


for _ in range(voltex):
    temp_node, temp_voltex = map(int, input().rstrip().split())
    graph[temp_node].append(temp_voltex)
    graph[temp_voltex].append(temp_node)


for connections in graph:
    connections.sort()

visited = [False] * (node + 1)
# 각 노드의 방문 순서를 기록하는 리스트 초기화
order = [0] * (node + 1)
# 방문 순서 카운트
count = 1

# 수정된 부분: 시작 노드의 방문 순서를 먼저 기록
order[start] = count
count += 1

# deque로 삽입.
queue = deque([start])
# 현재 노드 방문 처리
visited[start] = True
# 큐가 빌 때까지 반복
while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    current = queue.popleft()

    # 현재 노드와 연결된 노드들을 큐에 추가
    for adj in graph[current]:
        if not visited[adj]:
            visited[adj] = True  # 방문 처리
            order[adj] = count  # 방문 순서 기록
            count += 1  # 방문 순서 증가
            queue.append(adj)

# 각 노드의 방문 순서 출력
for i in range(1, node + 1):
    print(order[i])
