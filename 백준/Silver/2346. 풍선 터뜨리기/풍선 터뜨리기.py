from collections import deque

N = int(input())
balloons = deque([(idx, val) for idx, val in enumerate(map(int, input().split()), start=1)])
result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(str(idx))
    
    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(' '.join(result))
