class Solution {
    public int[] solution(int[] numbers, String direction) {
        // 오른쪽으로 회전하는 경우
        if (direction.equals("right")) {
            int last = numbers[numbers.length - 1]; // 마지막 값 저장
            // 배열의 마지막 값을 제외한 나머지 요소들을 한 칸씩 오른쪽으로 이동
            for (int i = numbers.length - 1; i > 0; i--) {
                numbers[i] = numbers[i - 1];
            }
            numbers[0] = last; // 저장한 마지막 값을 맨 앞에 넣기
        }
        // 왼쪽으로 회전하는 경우
        else if (direction.equals("left")) {
            int first = numbers[0]; // 첫 번째 값 저장
            // 배열의 첫 번째 값을 제외한 나머지 요소들을 한 칸씩 왼쪽으로 이동
            for (int i = 0; i < numbers.length - 1; i++) {
                numbers[i] = numbers[i + 1];
            }
            numbers[numbers.length - 1] = first; // 저장한 첫 번째 값을 맨 뒤에 넣기
        }
        return numbers;
    }
}