def solution(board, moves):
    stk = []
    count = 0
    for move in moves:
        # 각 열의 상단부터 훑기.
        for i in range(len(board[0])):
            # 처음 0 이 아닌 값이 나오면
            # 그 값을 빼서 stk에 넣고 그 위치는 0으로
            if board[i][move - 1] != 0:
                if stk and stk[-1] == board[i][move - 1]:
                    stk.pop()
                    board[i][move - 1] = 0
                    count += 2
                    break
                else:
                    stk.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    break

    return count