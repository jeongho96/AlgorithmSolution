
from sys import stdin
from heapq import *

input = stdin.readline

N = int(input().rstrip())

heap = []
for i in range(N):
    card = int(input().rstrip())
    heappush(heap, card)

result = 0

while True:
    
    if len(heap) == 1:
        break
        
    if heap:
        x = heappop(heap)
        y = heappop(heap)
        result += x + y
        heappush(heap, x + y)

    

print(result)