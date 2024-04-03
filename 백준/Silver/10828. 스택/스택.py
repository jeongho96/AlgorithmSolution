
from sys import stdin

input = stdin.readline

N = int(input().rstrip())

stack = []
result = []
for _ in range(N):
    line = input().rstrip().split()

    if len(line) == 1:
        order = line[0]
    else:
        order, value = line
        value = int(value)

    if order == 'push':
        stack.append(value)
    elif order == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif order == 'size':
        result.append(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif order == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

print(*result, sep='\n')