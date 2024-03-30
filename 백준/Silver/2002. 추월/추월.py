from collections import deque
from sys import stdin

input = stdin.readline

N = int(input().rstrip())
enter = deque()
count = 0


for _ in range(N):
    enter.append(input().rstrip())

for _ in range(N):
    exit_car = input().rstrip()  # 터널에서 나오는 차량
    if exit_car != enter[0]:
        enter.remove(exit_car)
        count += 1
    else:
        enter.popleft()


print(count)