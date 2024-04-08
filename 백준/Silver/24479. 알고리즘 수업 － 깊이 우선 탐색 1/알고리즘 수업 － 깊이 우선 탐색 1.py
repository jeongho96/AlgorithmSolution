from sys import stdin

input = stdin.readline

node, voltex, start = map(int, input().rstrip().split())
graph = [[] for _ in range(node + 1)]
for _ in range(voltex):
    temp_node, temp_voltex = map(int, input().rstrip().split())
    graph[temp_node].append(temp_voltex)
    graph[temp_voltex].append(temp_node)

for connections in graph:
    connections.sort(reverse=True)  # 스택을 사용하기 때문에 역순으로 정렬

visited = [False] * (node + 1)
order = [0] * (node + 1)
count = 1

stack = [start]

while stack:
    current = stack.pop()
    if not visited[current]:
        visited[current] = True
        order[current] = count
        count += 1
        for adj in graph[current]:
            if not visited[adj]:
                stack.append(adj)

for i in range(1, node + 1):
    print(order[i])
