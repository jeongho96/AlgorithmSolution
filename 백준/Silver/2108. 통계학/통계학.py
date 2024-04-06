
from sys import stdin
from collections import Counter


input = stdin.readline

N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]

def arithmetic_mean(numbers):
    return round(sum(numbers) / len(numbers))

def center_number(numbers):
    center_numbers = sorted(numbers)
    return center_numbers[(len(center_numbers) - 1) // 2]

def max_count(numbers):
    counter = Counter(numbers).most_common()
    answer_list = []
    for i in counter:
        if counter[0][1] == i[1]:
            answer_list.append(i[0])

    if len(answer_list) == 1:
        return answer_list[0]
    else:
        return sorted(answer_list)[1]

def range_numbers(numbers):
    return max(numbers) - min(numbers)


print(arithmetic_mean(numbers))
print(center_number(numbers))
print(max_count(numbers))
print(range_numbers(numbers))
