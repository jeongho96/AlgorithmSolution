from sys import stdin

input = stdin.readline

# 입력값 1 딕셔너리의 길이이자 키값

N = int(input().rstrip())
switch = dict()

for i in range(1, N + 1):
    switch[i] = 0

# 입력값 2 스위치의 상태이자 딕셔너리의 밸류
value_list = list(map(int, input().rstrip().split()))
for i in range(1, N + 1):
    switch[i] = value_list[i - 1]

switch_key = list(switch.keys())

# 학생 수
student_count = int(input().rstrip())

# 학생 수 만큼 성별과 받은 숫자
for i in range(student_count):
    student, switch_number = map(int, input().rstrip().split())
    if student == 1:
        for j in range(1, len(switch_key) + 1):
            if switch_key[j - 1] % switch_number == 0:
                switch[j] = 1 if switch[j] == 0 else 0
    if student == 2:
        # 자신의 상태는 무조건 변경
        switch[switch_number] = 1 if switch[switch_number] == 0 else 0
        for j in range(1, len(switch_key) // 2 + 1):
            left = switch_number - j
            right = switch_number + j
            if left < 1 or right > len(switch_key) or switch[left] != switch[right]:
                break

            switch[left] = 1 if switch[left] == 0 else 0
            switch[right] = 1 if switch[right] == 0 else 0

for i in range(0, len(switch.values()), 20):
    print(*(list(switch.values())[i:i+20]), sep=" ")
