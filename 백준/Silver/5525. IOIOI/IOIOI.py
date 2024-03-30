from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

check_string = 'O'.join(('I' * (N + 1)))
count = 0

for i in range(len(S)):
    if S[i:i+len(check_string)] == check_string:
        if i+len(check_string) <= len(S):
            count += 1

print(count)