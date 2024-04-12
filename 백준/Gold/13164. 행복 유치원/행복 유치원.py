from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

heights = list(map(int, input().split()))
heights.sort()

# 인접한 학생들 사이의 키 차이 계산
differences = []
for i in range(1, N):
    differences.append(heights[i] - heights[i-1])

# 차이를 내림차순으로 정렬
differences.sort(reverse=True)

# 가장 큰 K-1개 차이를 제외한 나머지 차이들의 합 계산
min_cost = sum(differences[K-1:]) if K < N else 0

print(min_cost)
