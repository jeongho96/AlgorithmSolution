N = int(input())

score_list = list(map(int, input().split()))
answer_list = []

for i in score_list:
    answer_list.append(i/max(score_list) * 100)

print(sum(answer_list) / len(answer_list))