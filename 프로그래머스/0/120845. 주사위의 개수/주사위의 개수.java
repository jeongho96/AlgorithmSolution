class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;

        // 각각의 차원에서 들어갈 수 있는 주사위 개수를 구한다.
        // 그리고 그 값을 모두 곱하면 정답

        int width = box[0] / n;
        int height = box[1] / n;
        int length = box[2] / n;
        
        answer = width * height * length;
        

        return answer;
    }
}