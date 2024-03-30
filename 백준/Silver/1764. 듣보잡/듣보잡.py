from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())
N_set = set()  # 집합으로 변경
answer = []
cnt = 0

for _ in range(N):
    person = input().rstrip()
    N_set.add(person)  # 리스트 대신 집합에 추가

for _ in range(M):
    person = input().rstrip()
    if person in N_set:  # 집합에서 요소의 존재 여부를 확인
        answer.append(person)
        cnt += 1

answer.sort()
print(cnt)
print(*answer, sep='\n')
