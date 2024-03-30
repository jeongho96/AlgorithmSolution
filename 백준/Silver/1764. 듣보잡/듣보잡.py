# 43924KB, 88ms

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

notHear = set()
for _ in range(N):
    notHear.add(input())

notSee = set()
for _ in range(M):
    notSee.add(input())

answer = sorted(list(notHear & notSee))

print(len(answer))
print(''.join(answer), end = '')