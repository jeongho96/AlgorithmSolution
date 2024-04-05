from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

immigration = [int(input().rstrip()) for _ in range(N)]

start_time, end_time = 1, max(immigration) * M

# 이진 탐색 시작.
while start_time <= end_time:
    middle_time = (start_time + end_time) // 2

    # 해당 시간으로 입국심사를 통과하는 사람의 수를 구하기.
    target = sum(middle_time // time for time in immigration)

    # 시간이 너무 짧아서 처리할 시간이 모자름.
    if target < M:
        start_time = middle_time + 1
    # 주어진 시간이 충분함. 줄여도 됨.
    else:
        end_time = middle_time - 1

print(start_time)