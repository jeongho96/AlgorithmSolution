from itertools import permutations
from sys import stdin
read = stdin.readline

n, m = map(int, read().split())

# 1부터 n까지의 숫자 리스트 생성
nums = [i for i in range(1, n+1)]

# nums 리스트에서 m개를 선택하는 모든 순열을 구함
perms = permutations(nums, m)

# 구한 순열을 출력
for perm in perms:
    print(' '.join(map(str, perm)))
