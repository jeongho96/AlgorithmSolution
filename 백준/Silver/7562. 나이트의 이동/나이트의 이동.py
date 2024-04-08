from collections import deque

# 나이트가 이동할 수 있는 8가지 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(start_x, start_y, end_x, end_y, size):
    queue = deque()
    queue.append((start_x, start_y))
    visited = [[False] * size for _ in range(size)]
    visited[start_x][start_y] = True
    count = 0

    while queue:
        # 현재 위치에서의 모든 이동 가능한 위치 확인
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 목적지에 도달했다면 반환
            if x == end_x and y == end_y:
                return count
            # 8가지 방향에 대해 이동 가능한지 확인
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                # 유효한 위치인지, 방문하지 않은 위치인지 확인
                if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        # 이동 횟수 증가
        count += 1

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 체스판의 한 변의 길이 입력
    size = int(input())
    # 현재 위치와 목적지 입력
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    # 최소 이동 횟수 계산 후 출력
    print(bfs(start_x, start_y, end_x, end_y, size))
