from heapq import *
from sys import stdin

input = stdin.readline

n = int(input().rstrip())
num_heap = []
answer = []
for i in range(n):
    x = int(input().rstrip())

    if x:
        heappush(num_heap, x)

    else:
        if num_heap:
            answer.append(heappop(num_heap))
        else:
            answer.append(0)


print(*answer, sep='\n')
