import sys

input = sys.stdin.readline

N = int(input())

file_list = {}

for _ in range(N):
    _, extension = input().rstrip().split('.')
    file_list[extension] = file_list.get(extension, 0) + 1

for key, value in sorted(file_list.items()):
    print(f'{key} {value}')