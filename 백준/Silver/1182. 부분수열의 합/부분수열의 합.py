def backtrack(index, current_sum):
    global count  # 전역 변수 사용
    if index >= N:  # 수열의 끝에 도달했다면
        return
    current_sum += numbers_list[index]  # 현재 수를 합에 추가
    if current_sum == S:  # 현재까지의 합이 S와 같다면
        count += 1  # 경우의 수를 하나 증가
    # 현재 수를 포함시키는 경우
    backtrack(index + 1, current_sum)
    # 현재 수를 포함시키지 않는 경우
    backtrack(index + 1, current_sum - numbers_list[index])

# 입력 받기
N, S = map(int, input().split())
numbers_list = list(map(int, input().split()))

count = 0  # 조건을 만족하는 경우의 수
# 백트래킹 시작
backtrack(0, 0)  # 초기 인덱스와 합은 0

print(count)
