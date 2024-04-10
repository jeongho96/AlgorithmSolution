N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf') # 최소 비용을 저장할 변수

def backtrack(current, visited, total_cost):
    global min_cost
    
    # 모든 도시를 방문한 경우
    if len(visited) == N:
        # 시작 도시로 돌아갈 수 있다면 최소 비용 갱신
        if cost[current][0] > 0:
            min_cost = min(min_cost, total_cost + cost[current][0])
        return
    
    for next_city in range(N):
        if next_city not in visited and cost[current][next_city] > 0:
            # 현재까지의 비용이 이미 최소 비용보다 크거나 같은 경우 탐색 중단
            if total_cost + cost[current][next_city] >= min_cost:
                continue
            backtrack(next_city, visited + [next_city], total_cost + cost[current][next_city])

# 시작 도시에서부터 탐색 시작
backtrack(0, [0], 0)

print(min_cost)
