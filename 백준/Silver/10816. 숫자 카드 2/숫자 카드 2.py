# 141652kB, 624ms

from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input().rstrip())
sang_card = list(map(int, input().rstrip().split()))

sang_counter = Counter(sang_card)

M = int(input().rstrip())
check_card = list(map(int, input().rstrip().split()))
answer_list = [sang_counter[card] for card in check_card]

print(" ".join(map(str, answer_list)))