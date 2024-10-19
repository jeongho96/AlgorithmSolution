import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        int layer = 1;  // 현재 몇 번째 층에 있는지
        int range = 1;  // 방 번호의 범위, 1번 방부터 시작
        
        // N번 방이 포함된 층을 찾을 때까지 반복
        while (N > range) {
            range += 6 * layer;  // 계차수열로 방의 범위 증가
            layer++;
        }
        
        System.out.println(layer);
    }
}
