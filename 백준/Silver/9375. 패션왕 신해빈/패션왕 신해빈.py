
from sys import stdin
from itertools import combinations

input = stdin.readline

T = int(input().rstrip())

result = []
for i in range(T):
    N = int(input().rstrip())
    cloth_dict = {}
    for _ in range(N):
        cloth, cloth_type = input().rstrip().split()
        if cloth_type in cloth_dict:
            cloth_dict[cloth_type] += 1
        else:
            cloth_dict[cloth_type] = 1

    cloth_comb = 1  # 초기값은 아무 의상도 선택하지 않는 경우 1로 설정
    for cnt in cloth_dict.values():
        cloth_comb *= (cnt + 1)  # 해당 의상 종류를 선택하지 않는 경우를 포함하여 곱함
    result.append(cloth_comb - 1)  # 아무 의상도 선택하지 않는 경우를 뺌

print(*result, sep='\n')