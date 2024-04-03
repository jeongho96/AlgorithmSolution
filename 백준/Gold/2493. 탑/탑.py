# 입력 받기: 탑의 개수 및 각 탑의 높이
N = int(input())
towers = list(map(int, input().split()))
# 스택 초기화 및 정답을 저장할 리스트 초기화
stack = []
answer = [0] * N

# 모든 탑을 순회하면서
for i in range(N):
    # 현재 스택이 비어있지 않고, 스택의 맨 위에 있는 탑의 높이가 현재 탑의 높이보다 작은 경우
    while stack and stack[-1][1] < towers[i]:
        # 스택에서 해당 탑을 제거
        stack.pop()
    # 스택이 비어있지 않다면(즉, 현재 탑보다 높이가 큰 탑이 있다면)
    if stack:
        # 정답 리스트에 스택의 맨 위에 있는 탑의 인덱스 + 1을 저장
        answer[i] = stack[-1][0] + 1
    # 현재 탑을 스택에 추가
    stack.append((i, towers[i]))

# 정답 출력
print(' '.join(map(str, answer)))
