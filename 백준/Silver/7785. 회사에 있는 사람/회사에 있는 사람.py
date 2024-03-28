N = int(input())
enter_set = set()

for _ in range(N):
    name, log = input().split()
    if log == "enter":
        enter_set.add(name)
    else:  # log == "leave"
        enter_set.remove(name)

# 사전 역순으로 정렬하여 출력
for name in sorted(enter_set, reverse=True):
    print(name)
