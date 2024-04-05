from sys import stdin

input = stdin.readline

N = int(input().rstrip())

time_list = list(map(int, input().rstrip().split()))

time_list.sort()

sum = 0
index = 0
for i in range(N, 0, -1):


    if i == N:
        sum += time_list[0] * i
    else:
        # 직전 합을 구해서, 현재 인덱스의 값과 더하기.
        sum += i * time_list[index]

    index += 1

print(sum)
