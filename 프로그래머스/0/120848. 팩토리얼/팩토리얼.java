class Solution {
    public int solution(int n) {
        int factorial = 1;  // 팩토리얼 초기값
        int i = 1;          // 팩토리얼을 구하기 위한 카운터

        // n보다 작은 가장 큰 팩토리얼을 찾기 위한 루프
        while (factorial <= n) {
            i++; 
            factorial *= i;
        }

        // 루프를 빠져나오면 n을 넘었으므로, i-1 번째 팩토리얼이 답
        return i - 1;
    }
}