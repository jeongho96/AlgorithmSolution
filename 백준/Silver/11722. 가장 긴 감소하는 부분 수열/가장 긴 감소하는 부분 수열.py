from sys import stdin
input = stdin.readline


# 최장 길이 감소하는 부분 배열 기준으로 찾기
def lis(nums):
    n = len(nums)

    dp = [1] * n

    for i in range(1 , n):
        for j in range(i):
            # 비교해서 num[i] 가 더 큰 경우에만 처리
            if nums[i] < nums[j]:
                # nums[i]를 이용하여 만든 부분 수열의 길이와
                # nums[j]를 이용하여 만든 부분 수열의 길이 + 1 중 최댓값 저장.
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

n = int(input())
sequence = list(map(int, input().split()))

print(lis(sequence))