from sys import stdin

input = stdin.readline

a1, a0 = map(int, input().rstrip().split())

c = int(input().rstrip())

n0 = int(input().rstrip())

if (a0 <= (c - a1) * n0) and a1 <= c:
    print(1)
else:
    print(0)

