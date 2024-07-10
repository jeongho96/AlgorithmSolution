import math


def solution(progresses, speeds):
    answer = []
    days_left = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]

    print(days_left)  # 남은 일수를 확인

    current_day = days_left[0]
    count = 0

    for day in days_left:
        if day > current_day:
            answer.append(count)
            current_day = day
            count = 1
        else:
            count += 1

    answer.append(count)  # 마지막 배포 묶음 추가

    return answer
