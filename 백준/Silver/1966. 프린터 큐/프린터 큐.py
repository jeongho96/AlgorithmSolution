from sys import stdin
from collections import deque

input = stdin.readline

T = int(input().rstrip())
answer_list = []

for _ in range(T):
    doc_count, target = map(int, input().rstrip().split())
    priorities = list(map(int, input().rstrip().split()))
    queue = deque(enumerate(priorities))

    answer = 0

    while queue:
        # 현재 큐의 가장 앞에 있는 문서의 중요도가 최대 중요도와 같은지 확인
        if queue[0][1] == max(priorities):
            answer += 1
            printed = queue.popleft()
            priorities.remove(printed[1])

            if printed[0] == target:
                answer_list.append(answer)
                break
        else:
            queue.append(queue.popleft())

print(*answer_list, sep='\n')
