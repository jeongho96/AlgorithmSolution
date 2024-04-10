from sys import stdin
from itertools import combinations
input = stdin.readline

# 1. 숫자 리스트를 받는다.
N, S = map(int, input().split())

numbers_list = list(map(int, input().split()))
# 2. combination을 활용해 전체 개수 중에 i개씩 뽑아서 조합을 확인.
count = 0
for i in range(1, N + 1):
    for numbers in combinations(numbers_list, i):  # 각 i에 대한 조합을 생성
        if sum(numbers) == S:  # 조합의 합이 S와 같은 경우
            count += 1

print(count)
