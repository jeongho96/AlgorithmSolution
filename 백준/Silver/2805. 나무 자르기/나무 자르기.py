
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 1, max(tree_list)

# 이진 탐색 수행
result = 0
while start <= end:
    mid = (start + end) // 2  # 중간점을 절단기 높이로 설정

    # 중간점에서의 나무 길이 합계 계산
    wood = sum(tree - mid if tree > mid else 0 for tree in tree_list)

    # 만약 잘린 나무의 길이가 목표치(M)보다 크거나 같으면 더 높게 잘라도 됨
    if wood >= M:
        result = mid  # 이때의 중간값을 결과로 저장
        start = mid + 1
    else:
        end = mid - 1

print(result)