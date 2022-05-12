from collections import deque
n,k = map(int,input().split())

answer = []

circular_queue = deque([i for i in range(1, n+1)])

for _ in range(0, n):
    circular_queue.rotate(-k + 1)
    answer.append(circular_queue.popleft())

print('<',end='')
print(*answer,sep=', ',end='')
print('>')
