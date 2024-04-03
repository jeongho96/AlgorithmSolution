from sys import stdin

input = stdin.readline

K = int(input().rstrip())

stack = []

for _ in range(K):
    n = int(input().rstrip())

    if n == 0:
        stack.pop()
    elif n != 0:
        stack.append(n)

print(sum(stack))