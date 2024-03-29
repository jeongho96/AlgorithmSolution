
from sys import stdin

input = stdin.readline

N = int(input().rstrip())
user_list = set()

total = 0

for _ in range(N):
    nickname = input().rstrip()
    if nickname == "ENTER": 
        user_list.clear()  
    else: 
        if nickname not in user_list: 
            total += 1
            user_list.add(nickname)

print(total)
