

from sys import stdin

read = stdin.readline

n, m = map(int, read().split())
answers = []
answer = []



def back_tracking(index, n, m, start):
    if index == m:
        answers.append(' '.join(map(str, answer)))
        return


    for i in range(start, n):
        answer.append(i + 1)

        back_tracking(index + 1, n, m, i + 1)
        answer.pop()


back_tracking(0, n, m, 0)
print('\n'.join(answers))
