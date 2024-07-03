def solution(arr):
    answer = []
    check_number = arr[0]
    for i in range(len(arr)):

        # 2. 이전 숫자와 중복이라면 패스
        # 이전 숫자와 같거나, 처음 값이 아니라면
        if (arr[i] == check_number) and (i != 0):
            continue

        # 1. 반복문을 순회하며 처음보는 숫자는 배열에 저장.
        answer.append(arr[i])

        # 3. 중복이 아니라면 추가하고 체크하는 숫자를 변경
        check_number = arr[i]

    return answer