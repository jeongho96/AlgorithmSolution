import sys
from heapq import *

input = sys.stdin.readline

T = int(input().rstrip())
result = []

for t in range(T):
    N = int(input().rstrip())
    chapter_heap = list(map(int, input().rstrip().split()))
    heapify(chapter_heap)
    total = 0

    # 파일이 1개 이하일 때까지 합치기
    while len(chapter_heap) > 1:
        # 가장 작은 두 파일 선택하여 합치기
        merged_file = heappop(chapter_heap) + heappop(chapter_heap)
        total += merged_file
        # 합친 파일을 다시 최소 힙에 추가
        heappush(chapter_heap, merged_file)

    result.append(total)

print(*result, sep='\n')
