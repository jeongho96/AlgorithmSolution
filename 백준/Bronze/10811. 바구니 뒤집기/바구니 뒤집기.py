from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

box = [i for i in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    box[a-1:b] = reversed(box[a-1:b])

print(*box)
