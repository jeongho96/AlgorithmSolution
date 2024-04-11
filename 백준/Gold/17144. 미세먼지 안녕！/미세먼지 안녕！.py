R, C, T = map(int, input().split())  # R: 행의 수, C: 열의 수, T: 시뮬레이션 시간
A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기의 위치를 찾습니다.
air_cleaner = []
for i in range(R):
    if A[i][0] == -1:
        air_cleaner.append(i)

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 dx, dy 정의
dy = [0, 0, -1, 1]

# 미세먼지 확산 함수
def spread():
    temp = [[0] * C for _ in range(R)]  # 확산된 후의 미세먼지 상태를 저장할 임시 배열
    for x in range(R):
        for y in range(C):
            if A[x][y] > 0:
                spread_amount = A[x][y] // 5  # 확산되는 미세먼지 양
                spread_count = 0
                for direction in range(4):
                    nx, ny = x + dx[direction], y + dy[direction]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        temp[nx][ny] += spread_amount
                        spread_count += 1
                A[x][y] -= spread_amount * spread_count
    # 확산된 미세먼지를 원래 배열에 추가합니다.
    for i in range(R):
        for j in range(C):
            A[i][j] += temp[i][j]

# 공기청정기 작동 함수
def clean():
    upper, lower = air_cleaner

    # 위쪽 공기청정기 작동
    for i in range(upper - 1, 0, -1):
        A[i][0] = A[i - 1][0]
    for i in range(C - 1):
        A[0][i] = A[0][i + 1]
    for i in range(upper):
        A[i][C - 1] = A[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        A[upper][i] = A[upper][i - 1]
    A[upper][1] = 0  # 공기청정기 바로 옆은 항상 0

    # 아래쪽 공기청정기 작동
    for i in range(lower + 1, R - 1):
        A[i][0] = A[i + 1][0]
    for i in range(C - 1):
        A[R - 1][i] = A[R - 1][i + 1]
    for i in range(R - 1, lower, -1):
        A[i][C - 1] = A[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        A[lower][i] = A[lower][i - 1]
    A[lower][1] = 0  # 공기청정기 바로 옆은 항상 0

# T번 시뮬레이션 실행
for _ in range(T):
    spread()  # 미세먼지 확산
    clean()  # 공기청정기 작동

# 결과 출력
result = sum(sum(row) for row in A) + 2  # 공기청정기 위치를 -1로 표시했으므로, 마지막에 2를 더해줍니다.
print(result)
