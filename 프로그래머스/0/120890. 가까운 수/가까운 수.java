class Solution {
    public int solution(int[] array, int n) {
        int minDiff = Integer.MAX_VALUE;  // 가장 작은 차이값을 저장할 변수
        int closestValue = 0;  // 가장 가까운 값을 저장할 변수
        for(int i = 0; i < array.length; i++){

            int diff = Math.abs(array[i] - n);  // 배열의 값과 n의 차이의 절대값을 계산

            // 차이가 더 작거나, 차이가 같지만 배열의 값이 더 작은 경우
            if (diff < minDiff || (diff == minDiff && array[i] < closestValue)) {
                minDiff = diff;
                closestValue = array[i];
            }
        }

        return closestValue;
    }
}