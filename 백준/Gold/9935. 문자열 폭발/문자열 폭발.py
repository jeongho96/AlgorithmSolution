s = input()  # 원본 문자열 입력 받기
bomb = input()  # 폭발 문자열 입력 받기
last_char = bomb[-1]  # 폭발 문자열의 마지막 문자
stack = []  # 스택 역할을 할 리스트

for char in s:
    stack.append(char)  # 스택에 문자 추가
    # 현재 스택의 상태가 폭발 문자열로 끝나는지 확인
    if char == last_char and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]  # 폭발 문자열을 스택에서 제거

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
