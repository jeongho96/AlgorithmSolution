from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())
N_set = set(input().rstrip() for _ in range(N))
M_set = set(input().rstrip() for _ in range(M))

# 두 집합의 교집합을 구한 후 리스트로 변환하고 정렬
answer = sorted(list(N_set & M_set))

print(len(answer))
print('\n'.join(answer))