class Solution {
    public int solution(int[][] dots) {
        // 기울기 계산 함수
        double slope1 = calculateSlope(dots[0], dots[1]);
        double slope2 = calculateSlope(dots[2], dots[3]);

        double slope3 = calculateSlope(dots[0], dots[2]);
        double slope4 = calculateSlope(dots[1], dots[3]);

        double slope5 = calculateSlope(dots[0], dots[3]);
        double slope6 = calculateSlope(dots[1], dots[2]);

        // 기울기 비교해서 평행한 직선이 있으면 1 반환
        if (slope1 == slope2 || slope3 == slope4 || slope5 == slope6) {
            return 1;
        }

        // 평행한 직선이 없으면 0 반환
        return 0;
    }

    // 기울기 계산 함수
    private double calculateSlope(int[] dot1, int[] dot2) {
        int x1 = dot1[0], y1 = dot1[1];
        int x2 = dot2[0], y2 = dot2[1];
        
        // x값이 같으면 기울기는 무한대 (수직선)
        if (x1 == x2) {
            return Double.POSITIVE_INFINITY;
        }

        return (double) (y2 - y1) / (x2 - x1);  // 기울기 계산
    }
}
