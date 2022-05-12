from collections import deque
N = int(input())
N_list = deque([i for i in range(N,0,-1)])

while True:
    if len(N_list) == 1:
        break
    N_list.pop()
    N_list.appendleft(N_list[-1])
    N_list.pop()

print(N_list[0])