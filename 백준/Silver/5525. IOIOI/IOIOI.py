from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

answer = 0
count = 0

i = 0
while i <= (M-2):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0
print(answer)