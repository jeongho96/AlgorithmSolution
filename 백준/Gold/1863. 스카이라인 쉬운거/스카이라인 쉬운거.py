from sys import stdin

input = stdin.readline

n = int(input())
skyline = []

for i in range(n):
    x, y = map(int, input().split())
    skyline.append((x, y))

stk = []
count = 0
# skyline 리스트 순회 코드 아래에, 마지막으로 '0' 높이 처리를 추가
for _, y in skyline + [(0, 0)]:  # 마지막에 높이 0을 추가하여 모든 높이 처리
    while stk and y < stk[-1]:
        stk.pop()
        count += 1
    if not stk or y > stk[-1]:
        stk.append(y)

print(count)
