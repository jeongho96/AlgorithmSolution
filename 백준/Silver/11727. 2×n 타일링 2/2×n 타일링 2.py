def solution(n):
    # dp 테이블 초기화
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1:
        dp[2] = 3  # n이 2 이상일 때만 dp[2]를 설정

    # 가로 길이가 3부터 n까지의 각각의 경우에 대해 바닥을 채우는 방법의 수 계산
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007
    
    return dp[n]

# 사용자 입력 받기
n = int(input())

# 결과 출력
print(solution(n))