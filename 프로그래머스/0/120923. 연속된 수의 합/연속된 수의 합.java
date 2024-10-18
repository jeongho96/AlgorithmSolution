class Solution {
    public int[] solution(int num, int total) {
        // 연속된 정수의 평균값 계산
        int avg = total / num;
        // 첫 번째 값 계산
        int start = avg - (num - 1) / 2;
        // 연속된 num개의 정수 배열 생성
        int[] result = new int[num];

        for (int i = 0; i < num; i++) {
            result[i] = start + i;
        }

        return result;
    }
}