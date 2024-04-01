from collections import Counter

def operation(arr):
    max_length = 0
    new_arr = []
    for row in arr:
        counter = Counter(row)
        if counter.get(0):
            del counter[0]  # 0은 제외
        sorted_row = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for number, count in sorted_row:
            new_row += [number, count]
        max_length = max(max_length, len(new_row))
        new_arr.append(new_row)

    for row in new_arr:
        row += [0] * (max_length - len(row))  # 빈 공간 0으로 채우기

    return new_arr

def solution(r, c, k):
    arr = [list(map(int, input().split())) for _ in range(3)]
    for time in range(101):
        if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
            return time
        if len(arr) >= len(arr[0]):
            arr = operation(arr)  # R 연산
        else:
            arr = list(zip(*arr))  # 행렬 전치
            arr = operation(arr)
            arr = list(zip(*arr))  # 다시 행렬 전치
    return -1

r, c, k = map(int, input().split())
print(solution(r, c, k))
