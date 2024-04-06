
from sys import stdin

input = stdin.readline

X , Y = map(int, input().rstrip().split())

target = 0

# 입력 제한수치까지 받기.
start, end = 1, 1000000000
Z = (Y * 100) // X

# 변하지 않는 값 기준
answer = -1

while start <= end:
    mid = (start + end) // 2

    # 더 판수를 늘린 확률이 기존 확률보다 크면
    if (((Y + mid) * 100) // (X + mid)) > Z:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1


if Z >= 99:
    print(-1)
else:
    print(answer)
