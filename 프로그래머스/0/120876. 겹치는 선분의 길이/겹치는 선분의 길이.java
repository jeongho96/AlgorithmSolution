import java.util.Arrays;

class Solution {
    public int solution(int[][] lines) {
        // -100부터 100까지 범위의 선분을 나타내기 위해 배열을 선언
        int[] lineOverlap = new int[201];  // 좌표 범위가 -100부터 100까지이므로

        // 각 선분의 시작과 끝에 해당하는 구간을 +1, -1로 표시
        for (int[] line : lines) {
            int start = Math.min(line[0], line[1]);
            int end = Math.max(line[0], line[1]);

            for (int i = start + 100; i < end + 100; i++) {
                lineOverlap[i]++;
            }
        }

        // 겹친 부분이 2개 이상인 구간의 길이를 계산
        int overlapLength = 0;
        for (int i = 0; i < lineOverlap.length; i++) {
            if (lineOverlap[i] > 1) {
                overlapLength++;
            }
        }

        return overlapLength;
    }
}