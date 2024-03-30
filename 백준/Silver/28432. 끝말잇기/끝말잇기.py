from sys import stdin
input = stdin.readline

# 끝말잇기 기록 입력
N = int(input().rstrip())
word_list = []
question_index = -1

for i in range(N):
    word = input().rstrip()
    word_list.append(word)
    if word == "?":
        question_index = i

# '?' 전후 단어 확인
first_word = word_list[question_index - 1][-1] if question_index > 0 else ""
last_word = word_list[question_index + 1][0] if question_index < N - 1 else ""

# 후보 단어 입력 및 검증
M = int(input().rstrip())
answer = ""
for _ in range(M):
    word = input().rstrip()

    # 기록에 존재하지 않고, 조건에 맞는 단어 찾기
    if word not in word_list:
        if (first_word == "" or word[0] == first_word) and (last_word == "" or word[-1] == last_word):
            answer = word
            break  # 조건을 만족하는 첫 번째 단어를 찾으면 반복 종료

print(answer)
