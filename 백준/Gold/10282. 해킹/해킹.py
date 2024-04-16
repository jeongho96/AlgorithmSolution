import heapq
import sys

input = sys.stdin.readline


INF = int(1e9)

t = int(input().rstrip())
results = []


for _ in range(t):
    n, d, c = map(int, input().rstrip().split())

    graph = [[] for _ in range(n + 1)]

    # 모든 의존성 정보를 입력받기 (단방향 그래프)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))  # b가 감염되면 a가 s초 후 감염됨

    # 최단 거리 테이블 무한대로 초기화
    distance = [INF] * (n + 1)


    # 다익스트라 알고리즘 수행
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


    # 다익스트라 알고리즘을 사용해 c번 컴퓨터부터 시작
    dijkstra(c)

    # 감염된 컴퓨터 수와 최대 걸린 시간 계산
    count = 0
    max_dist = 0
    for dist in distance:
        if dist < INF:
            count += 1
            if dist > max_dist:
                max_dist = dist

    # 결과 저장
    results.append(f"{count} {max_dist}")

# 결과 출력
for result in results:
    print(result)