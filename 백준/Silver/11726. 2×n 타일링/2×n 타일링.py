def solution(n):
    if n == 1:
        return 1
    # 바닥의 가로 길이가 2인 경우, 바닥을 채우는 방법은 2개
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    # 가로 길이가 3부터 n까지의 각각의 경우에 대해 바닥을 채우는 방법의 수
    for i in range(3, n + 1):
        # dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    
    return dp[n]


n = int(input())

print(solution(n))