from sys import stdin

input = stdin.readline

N = int(input().rstrip())

space = [input().rstrip() for _ in range(N)]

width_answer = 0
length_answer = 0

# 가로 방향 계산
for i in range(N):
    width_count = 0
    for j in range(N):
        if space[i][j] == '.':
            width_count += 1
        else:
            if width_count >= 2:
                width_answer += 1
            width_count = 0
    if width_count >= 2:  
        width_answer += 1

# 세로 방향 계산
for i in range(N):
    length_count = 0
    for j in range(N):
        if space[j][i] == '.':
            length_count += 1
        else:
            if length_count >= 2:
                length_answer += 1
            length_count = 0
    if length_count >= 2:  
        length_answer += 1

print(width_answer, length_answer)