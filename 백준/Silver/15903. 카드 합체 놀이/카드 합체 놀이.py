from sys import stdin
from heapq import *

input = stdin.readline

N,M = map(int,input().rstrip().split())


number_list = list(map(int,input().rstrip().split()))

heapify(number_list)
# 1. 한번 덮어씌우는 연산을 했을 때, 두 숫자의 합이 더 작은 값을 기준으로 잡아야 함.
# 2. 가능하면 작은 숫자들을 기준으로 합하는게 제일 좋음.

for i in range(M):
    x = heappop(number_list)
    y = heappop(number_list)

    heappush(number_list, x+y)
    heappush(number_list, x+y)


print(sum(number_list))