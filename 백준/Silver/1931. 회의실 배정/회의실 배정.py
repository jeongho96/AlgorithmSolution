from sys import stdin
input = stdin.readline

n = int(input().rstrip())
time_list = []
for i in range(n):
    time_list.append(tuple(map(int, input().rstrip().split())))

time_list.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 오름차순, 시작 시간 오름차순으로 정렬

count = 1
before_end = time_list[0][1]
for i in range(1, n):
    start, end = time_list[i]
    if before_end <= start:
        before_end = end
        count += 1

print(count)
