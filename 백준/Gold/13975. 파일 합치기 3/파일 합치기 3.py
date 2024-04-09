from sys import stdin
from heapq import *

input = stdin.readline


T = int(input().rstrip())
result = []
for t in range(T):
    N = int(input().rstrip())
    chapter_heap = list(map(int, input().rstrip().split()))
    heapify(chapter_heap)
    total = 0
    # 2개 미만이 될때까지
    while len(chapter_heap) > 1:
        # 가장 작은 두 파일 선택
        first = heappop(chapter_heap)
        second = heappop(chapter_heap)

        # 선택된 두 파일 합치기
        merged_file = first + second
        total += merged_file

        # 합친 파일을 다시 큐에 추가
        heappush(chapter_heap, merged_file)

    result.append(total)

print(*result, sep='\n')