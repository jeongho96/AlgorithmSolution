N = int(input())

file_list = {}

for i in range(N):
    name, extension = map(str, input().split('.'))
    if file_list.get(extension) is None:
        file_list[extension] = 1
    else:
        file_list[extension] += 1
        
for key,value in sorted(file_list.items()):
    print(f"{key} {value}")