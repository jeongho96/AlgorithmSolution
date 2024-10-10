class Solution {
    public int solution(int[][] dots) {
        int width = 0;
        int height = 0;


        for(int i = 1; i < dots.length; i++){
            // 대각선 찾기
            if(dots[0][0] != dots[i][0]){
                width = dots[i][0];
            }

            if(dots[0][1] != dots[i][1]){
                height = dots[i][1];
            }
        }

        width = Math.abs(width - dots[0][0]);
        height = Math.abs(height - dots[0][1]);



        return width * height;
    }
}