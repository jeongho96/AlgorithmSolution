n = int(input())
tower_heights = list(map(int, input().split()))

stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower_heights[i]:
            result.append(stack[-1][0] + 1)
            break
        stack.pop()
    if not stack:
        result.append(0)
    stack.append((i, tower_heights[i]))

print(*result)
