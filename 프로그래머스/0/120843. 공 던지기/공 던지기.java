class Solution {
    public int solution(int[] numbers, int k) {
        int index = (k - 1) * 2 % numbers.length;  // 순환을 고려한 인덱스 계산
        return numbers[index];
    }
}