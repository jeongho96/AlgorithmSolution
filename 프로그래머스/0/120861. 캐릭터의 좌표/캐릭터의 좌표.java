class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0,0};
        int limitX = board[0] / 2;
        int limitY = board[1] / 2;

        for (int i = 0; i < keyinput.length; i++) {
            switch (keyinput[i]) {
                case "left":
                    answer[0]--;
                    if (answer[0] < -limitX) answer[0] = -limitX;
                    break; // break 추가
                case "right":
                    answer[0]++;
                    if (answer[0] > limitX) answer[0] = limitX;
                    break; // break 추가
                case "up":
                    answer[1]++;
                    if (answer[1] > limitY) answer[1] = limitY;
                    break; // break 추가
                case "down":
                    answer[1]--;
                    if (answer[1] < -limitY) answer[1] = -limitY;
                    break; // break 추가
            }
        }

        return answer;
    }
}