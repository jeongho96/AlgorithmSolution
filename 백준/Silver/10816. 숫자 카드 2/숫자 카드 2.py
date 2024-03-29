from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input().rstrip())
sang_card = list(map(int, input().rstrip().split()))

sang_counter = Counter(sang_card)

M = int(input().rstrip())
check_card = list(map(int, input().rstrip().split()))
answer_list = []

for i in range(M):
    if sang_counter[check_card[i]] == 0:
        answer_list.append(0)
    else:
        answer_list.append(sang_counter[check_card[i]])

print(" ".join(map(str, answer_list)))

