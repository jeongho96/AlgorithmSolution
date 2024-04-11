def solution(board, moves):
    stk = []
    count = 0
    for move in moves:
        # 각 열의 상단부터 열을 기준으로 훑기.
        for i in range(len(board[0])):
            # 처음 0 이 아닌 값이 나오면
            if board[i][move - 1] != 0:
                picked = board[i][move - 1]
                board[i][move - 1] = 0
                # stack에 있는 값과 비교했을 때 같으면
                if stk and stk[-1] == picked:
                    stk.pop()
                    count += 2
                # 같지 않으면 추가만 해주기.
                else:
                    stk.append(picked)
                # 인형을 뽑았으니 다음 move로 이동
                break

    return count