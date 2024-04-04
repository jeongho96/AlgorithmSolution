from sys import stdin
from heapq import *
from collections import defaultdict

input = stdin.readline

T = int(input().rstrip())
answer_list = []

for _ in range(T):
    k = int(input().rstrip())
    max_heap = []
    min_heap = []
    check_dict = defaultdict(int)

    for _ in range(k):
        oper, val = input().rstrip().split()
        val = int(val)

        if oper == 'I':
            heappush(max_heap, -val)
            heappush(min_heap, val)
            check_dict[val] += 1
        elif oper == 'D':
            if val == 1:
                while max_heap:
                    pop_val = -heappop(max_heap)
                    if check_dict[pop_val] != 0:
                        check_dict[pop_val] -= 1
                        break
            elif val == -1:
                while min_heap:
                    pop_val = heappop(min_heap)
                    if check_dict[pop_val] != 0:
                        check_dict[pop_val] -= 1
                        break

    while max_heap:
        if check_dict[-max_heap[0]] == 0:
            heappop(max_heap)
        else:
            break

    while min_heap:
        if check_dict[min_heap[0]] == 0:
            heappop(min_heap)
        else:
            break

    if max_heap and min_heap:
        answer_list.append([-heappop(max_heap), heappop(min_heap)])
    else:
        answer_list.append('EMPTY')

for i in answer_list:
    if i == 'EMPTY':
        print(i)
    else:
        print(*i, sep=' ')
