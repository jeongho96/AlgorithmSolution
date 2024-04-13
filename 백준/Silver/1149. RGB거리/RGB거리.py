n = int(input())  # 집의 수
costs = [list(map(int, input().split())) for _ in range(n)]  # 각 집을 R, G, B로 칠하는 비용

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]

for i in range(1, n):
    # i번째 집을 R로 칠할 때의 최소 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # i번째 집을 G로 칠할 때의 최소 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    # i번째 집을 B로 칠할 때의 최소 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

# 마지막 집을 R, G, B로 칠했을 때의 최소 비용 중 최솟값이 정답
answer = min(dp[-1])
print(answer)
