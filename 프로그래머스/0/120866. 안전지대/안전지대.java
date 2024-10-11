class Solution {
    public int solution(int[][] board) {
            int n = board.length;
    int m = board[0].length;
    
    // 8방향을 나타내는 배열 (위, 아래, 왼쪽, 오른쪽, 대각선 4개)
    int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
    
    // 주변에 지뢰 표시를 2로 하기 위한 복사 배열
    int[][] newBoard = new int[n][m];
    
    // 기존 보드를 복사
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            newBoard[i][j] = board[i][j];
        }
    }

    // 지뢰가 있는 경우, 주변 8방향을 2로 표시
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 1) {
                for (int k = 0; k < 8; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    // 경계를 벗어나지 않는지 체크
                    if (ni >= 0 && ni < n && nj >= 0 && nj < m && newBoard[ni][nj] == 0) {
                        newBoard[ni][nj] = 2;  // 지뢰 주변을 2로 표시
                    }
                }
            }
        }
    }

    // 0의 개수를 세기
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (newBoard[i][j] == 0) {
                count++;
            }
        }
    }

    return count;
    }
}