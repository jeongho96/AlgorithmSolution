def distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def chicken_delivery(N, M, city, selected, idx):
    if len(selected) == M:
        total_distance = 0
        for house in houses:
            min_chicken_distance = float('inf')
            for idx in selected:
                min_chicken_distance = min(min_chicken_distance, distance(house, chicken_houses[idx]))
            total_distance += min_chicken_distance
        return total_distance
    
    if idx == len(chicken_houses):
        return float('inf')
    
    # 현재 치킨집을 선택하는 경우
    selected.append(idx)
    min_distance_with = chicken_delivery(N, M, city, selected, idx + 1)
    selected.pop()
    
    # 현재 치킨집을 선택하지 않는 경우
    min_distance_without = chicken_delivery(N, M, city, selected, idx + 1)
    
    return min(min_distance_with, min_distance_without)

if __name__ == "__main__":
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    
    chicken_houses = []
    houses = []
    
    # 치킨집과 집의 위치를 찾음
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken_houses.append((i, j))
            elif city[i][j] == 1:
                houses.append((i, j))
    
    selected = []
    result = chicken_delivery(N, M, city, selected, 0)
    
    print(result)
