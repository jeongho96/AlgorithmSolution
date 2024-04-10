import sys

input = sys.stdin.readline

target_channel = int(input())
m = int(input())
if m == 0:
    broken_number = []
else:
    broken_number = list(map(int, input().split()))

# 현재 채널(100)에서 + 혹은 -만 사용하여 이동하는 경우
# 현재 채널에서 target까지의 차이가 곧 최소값 중 가장 큰 값.
min_count = abs(100 - target_channel)

for number in range(1000000):
    number = str(number)

    for j in range(len(number)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(number[j]) in broken_number:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(number) - 1:
            min_count = min(min_count, abs(int(number) - target_channel) + len(number))


print(min_count)