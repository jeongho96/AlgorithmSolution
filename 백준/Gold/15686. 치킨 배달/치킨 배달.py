# 입력 처리
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집 위치 저장
houses = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

answer = float('inf')

# 치킨 거리 계산 함수
def get_chicken_distance(selected):
    distance = 0
    for hx, hy in houses:
        distance += min([abs(hx-cx) + abs(hy-cy) for cx, cy in selected])
    return distance

# 백트래킹을 이용한 치킨집 선택
def select_chicken(start, selected):
    global answer
    # 종료 조건: 선택한 치킨집이 M개일 때
    if len(selected) == M:
        answer = min(answer, get_chicken_distance(selected))
        return
    
    for i in range(start, len(chicken)):
        select_chicken(i+1, selected + [chicken[i]])

# 초기 치킨집 선택 시작
select_chicken(0, [])

print(answer)
