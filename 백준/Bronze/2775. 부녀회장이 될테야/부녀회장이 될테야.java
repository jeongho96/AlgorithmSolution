import java.io.IOException;
import java.util.Scanner;

public class Main {
    

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();  // 테스트 케이스 개수 입력

        for (int t = 0; t < T; t++) {
            int k = sc.nextInt();  // 층
            int n = sc.nextInt();  // 호

            // DP 테이블 초기화
            int[][] dp = new int[k + 1][n + 1];

            // 0층 초기화 (0층의 n호에는 n명이 산다)
            for (int i = 1; i <= n; i++) {
                dp[0][i] = i;
            }

            // DP 테이블 채우기
            for (int i = 1; i <= k; i++) {
                for (int j = 1; j <= n; j++) {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
                }
            }

            // k층 n호에 사는 사람 수 출력
            System.out.println(dp[k][n]);
        }

        sc.close();
    }
}
