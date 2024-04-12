import sys
import heapq  # 우선순위 큐를 사용하기 위해 heapq 모듈을 불러옵니다.

input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 이동을 위한 dx, dy 배열
dy = [0, 0, -1, 1]


def dijkstra(graph, n):
    distance = [[float('inf')] * n for _ in range(n)]  # 모든 지점까지의 최소 비용을 무한대로 초기화
    distance[0][0] = graph[0][0]  # 시작 지점의 비용을 초기화
    q = [(graph[0][0], 0, 0)]  # 우선순위 큐에 시작 지점을 삽입 (비용, x좌표, y좌표)

    while q:
        dist, x, y = heapq.heappop(q)  # 큐에서 최소 비용의 노드 정보를 추출
        if distance[x][y] < dist:  # 만약 현재 노드까지의 거리가 이미 더 짧은 경로로 계산되었다면 무시
            continue
        for i in range(4):  # 상, 하, 좌, 우 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 맵의 범위를 벗어나지 않는 경우
                cost = dist + graph[nx][ny]  # 해당 노드를 거쳐가는 비용 계산
                if cost < distance[nx][ny]:  # 만약 이 경로가 더 저렴하다면
                    distance[nx][ny] = cost  # 최소 비용 갱신
                    heapq.heappush(q, (cost, nx, ny))  # 우선순위 큐에 삽입
    return distance[n - 1][n - 1]  # 도착 지점까지의 최소 비용 반환


problem_number = 1
while True:
    n = int(input().rstrip())  # 지도의 크기 입력
    if n == 0:  # 입력의 종료 조건
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]  # 지도 정보 입력
    answer = dijkstra(graph, n)  # 다익스트라 알고리즘을 이용해 문제 해결
    print(f"Problem {problem_number}: {answer}")  # 결과 출력
    problem_number += 1
