from sys import stdin
from heapq import *

input = stdin.readline


N, H, T = map(int, input().split())

giant_heights = []

for i in range(N):
    heappush(giant_heights, -(int(input())))


count = 0
answer = 0
# 뿅망치 횟수만큼 꺼내서 확인
for i in range(T):

    # 키 리스트가 비어있지 않을 때
    if giant_heights:
        max_height = -heappop(giant_heights)

        # 가장 키가 큰 거인의 키가 H보다 크면
        if max_height >= H and max_height > 1:
            count += 1
            heappush(giant_heights, -(max_height / 2))
        # H가 만약 더 크면 값을 다시 그냥 넣기.
        else:
            heappush(giant_heights, -max_height)
            break
    else:
        break

# 작업을 다 한 뒤에도 거인의 최대 키가 더 크면 실패.
check = int(-heappop(giant_heights))
if check >= H:
    print("NO")
    print(check)
elif check < H:
    print("YES")
    print(count)
