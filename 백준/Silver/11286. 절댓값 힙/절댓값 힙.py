
from sys import stdin
from heapq import *

input = stdin.readline

n = int(input().rstrip())

heap = []

result = []
for i in range(n):
    x = int(input().rstrip())

    if x:
        heappush(heap, (abs(x), x))
    else:
        if not heap:
            result.append(0)
        else:
            _, x = heappop(heap)
            result.append(x)


print(*result, sep='\n')