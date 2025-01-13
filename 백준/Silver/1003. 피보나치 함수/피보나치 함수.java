import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 개수
        int T = sc.nextInt();

        // 피보나치 호출 횟수를 저장할 배열
        int[][] dp = new int[41][2]; // 0부터 40까지 저장

        // 초기값 설정
        dp[0][0] = 1; // fibonacci(0)에서 0의 호출 횟수는 1
        dp[0][1] = 0; // fibonacci(0)에서 1의 호출 횟수는 0
        dp[1][0] = 0; // fibonacci(1)에서 0의 호출 횟수는 0
        dp[1][1] = 1; // fibonacci(1)에서 1의 호출 횟수는 1

        // DP로 40까지 미리 계산
        for (int i = 2; i <= 40; i++) {
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]; // 0의 호출 횟수
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]; // 1의 호출 횟수
        }

        // 테스트 케이스 처리
        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            System.out.println(dp[n][0] + " " + dp[n][1]);
        }

        sc.close();
    }
}