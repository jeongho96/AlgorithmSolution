import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())

min_heap = []

for _ in range(N):
    row = list(map(int, input().rstrip().split()))
    for num in row:
        if len(min_heap) < N:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

# 최소 힙의 첫 번째 값이 N번째로 큰 값
print(min_heap[0])