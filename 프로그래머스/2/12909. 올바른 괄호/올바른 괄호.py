def solution(s):
    answer = []
    # 1. 괄호가 열기 전에 닫는 기호가 나올 경우
    if s[0] == ")":
        return False

    for i in range(len(s)):
        # 2. 괄호를 열었지만 개수만큼 닫지 않은 경우
        if s[i] == "(":
            answer.append("(")
        elif s[i] == ")" and len(answer) > 0:
            answer.pop()

    if len(answer) != 0:
        return False

    return True