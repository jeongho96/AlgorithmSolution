import sys

score_list = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
    "F": 0}

total = 0
avg_score = 0

for i in range(20):
    name, score, grade = sys.stdin.readline().split()
    score = float(score)
    if grade != 'P':
        total += score
        avg_score += score * score_list[grade]

print('%.6f' % (avg_score / total))