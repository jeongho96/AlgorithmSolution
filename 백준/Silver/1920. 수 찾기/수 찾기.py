from sys import stdin
input = stdin.readline

def binary_search(array, value):

    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (end + start) // 2
        if array[mid] == value:
            return 1
        elif array[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    return 0

N = int(input().rstrip())

array = list(map(int, input().rstrip().split()))
array.sort()
M = int(input().rstrip())

target_array = list(map(int, input().rstrip().split()))

for i in target_array:
    print(binary_search(array, i))