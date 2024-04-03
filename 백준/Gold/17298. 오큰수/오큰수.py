from sys import stdin

input = stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

stack = []
result = [-1] * N

for i, a in enumerate(A):
    while stack:
        if stack[-1][1] < a:
            j, _ = stack.pop()
            result[j] = a
        else:
            break
    stack.append((i, a))

print(*result)
