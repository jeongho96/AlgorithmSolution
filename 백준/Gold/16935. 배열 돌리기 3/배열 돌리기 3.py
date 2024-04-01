from sys import stdin

input = stdin.readline

n, m, r = map(int, input().rstrip().split())

matrix = [list(map(int, input().rstrip().split())) for i in range(n)]

numbers = list(map(int, input().rstrip().split()))


def operation1(matrix):
    return matrix[::-1]


def operation2(matrix):
    return [row[::-1] for row in matrix]


def operation3(matrix):
    result = [[0] * n for _ in range(m)]  # 회전한 결과를 표시하는 배열

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result


def operation4(matrix):
    result = [[0] * n for _ in range(m)]  # 회전한 결과를 표시하는 배열

    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = matrix[i][j]
    return result

def operation5(matrix):
    temp_matrix = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            # 1 -> 2
            temp_matrix[i][j + m//2] = matrix[i][j]
            # 2 -> 3
            temp_matrix[i + n//2][j + m//2] = matrix[i][j + m//2]
            # 3 -> 4
            temp_matrix[i + n//2][j] = matrix[i + n//2][j + m//2]
            # 4 -> 1
            temp_matrix[i][j] = matrix[i + n//2][j]
    return temp_matrix

def operation6(matrix):
    temp_matrix = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            # 1 -> 4
            temp_matrix[i + n // 2][j] = matrix[i][j]
            # 2 -> 1
            temp_matrix[i][j] = matrix[i][j + m // 2]
            # 3 -> 2
            temp_matrix[i][j + m // 2] = matrix[i + n // 2][j + m // 2]
            # 4 -> 3
            temp_matrix[i + n//2][j + m//2] = matrix[i + n//2][j]

    return temp_matrix


for number in numbers:
    if number == 1:
        matrix = operation1(matrix)
    elif number == 2:
        matrix = operation2(matrix)
    elif number == 3:
        matrix = operation3(matrix)
        n,m = m, n
    elif number == 4:
        matrix = operation4(matrix)
        n, m = m, n
    elif number == 5:
        matrix = operation5(matrix)
    elif number == 6:
        matrix = operation6(matrix)

for row in matrix:
    print(' '.join(map(str, row)))