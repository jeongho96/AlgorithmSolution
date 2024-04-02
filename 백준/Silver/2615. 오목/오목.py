N = 19
board = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터: 가로, 세로, 우하향, 우상향
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def check(x, y):
    if board[x][y] == 0:
        return False
    for i in range(4):
        cnt = 1
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == board[x][y]:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx[i] < N and 0 <= y - dy[i] < N and board[x - dx[i]][y - dy[i]] == board[x][y]:
                    break
                if 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < N and board[nx + dx[i]][ny + dy[i]] == board[x][y]:
                    continue
                return True
            nx += dx[i]
            ny += dy[i]
    return False

for i in range(N):
    for j in range(N):
        if check(i, j):
            print(board[i][j])
            print(i + 1, j + 1)
            exit(0)
print(0)
