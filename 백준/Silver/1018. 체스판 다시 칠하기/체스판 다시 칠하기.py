n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_changes(x, y, start_color):
    # 시작 색깔에 따라 변경해야 할 칸 수를 계산하는 함수
    change_count = 0
    color = start_color
    for i in range(x, x+8):
        for j in range(y, y+8):
            if board[i][j] != color:
                change_count += 1
            color = 'W' if color == 'B' else 'B'
        color = 'W' if color == 'B' else 'B'
    return change_count

min_changes = float('inf')
for i in range(n-7):
    for j in range(m-7):
        # 두 가지 시작 색깔에 대해 변경 횟수를 계산
        changes = min(count_changes(i, j, 'W'), count_changes(i, j, 'B'))
        min_changes = min(min_changes, changes)

print(min_changes)