n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
operations = list(map(int, input().split()))

def op1(arr):
    return arr[::-1]

def op2(arr):
    return [row[::-1] for row in arr]

def op3(arr):
    return list(zip(*arr[::-1]))

def op4(arr):
    return list(zip(*arr))[::-1]

def op5(arr):
    n = len(arr)
    m = len(arr[0])
    new_arr = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            new_arr[i][j+m//2] = arr[i][j]
            new_arr[i+n//2][j+m//2] = arr[i][j+m//2]
            new_arr[i+n//2][j] = arr[i+n//2][j+m//2]
            new_arr[i][j] = arr[i+n//2][j]
    return new_arr

def op6(arr):
    n = len(arr)
    m = len(arr[0])
    new_arr = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            new_arr[i+n//2][j] = arr[i][j]
            new_arr[i][j] = arr[i][j+m//2]
            new_arr[i][j+m//2] = arr[i+n//2][j+m//2]
            new_arr[i+n//2][j+m//2] = arr[i+n//2][j]
    return new_arr

for op in operations:
    if op == 1:
        arr = op1(arr)
    elif op == 2:
        arr = op2(arr)
    elif op == 3:
        arr = list(op3(arr))
        n, m = m, n
    elif op == 4:
        arr = list(op4(arr))
        n, m = m, n
    elif op == 5:
        arr = op5(arr)
    elif op == 6:
        arr = op6(arr)

for row in arr:
    print(' '.join(map(str, row)))
