N = int(input())
enter_log = {}
for i in range(N):
    name, log = map(str, input().split())
    enter_log[name] = log

answer_list = [key for key, value in enter_log.items() if value == "enter"]      

answer_list.sort(reverse=True)

for i in answer_list:
    print(i)
