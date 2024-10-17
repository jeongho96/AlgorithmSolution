import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력 처리를 빠르게 하기 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // N을 입력받음
        int N = Integer.parseInt(br.readLine());
        
        // 숫자의 범위가 1 ~ 10,000 이므로 카운팅 정렬을 위한 배열 선언
        int[] counting = new int[10001];  // 0은 사용하지 않음, 1 ~ 10000
        
        // 입력 숫자들을 카운트 배열에 기록
        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(br.readLine());
            counting[number]++;
        }
        
        // 결과를 출력하기 위해 StringBuilder 사용
        StringBuilder sb = new StringBuilder();
        
        // 카운팅 배열을 순회하면서 결과 출력
        for (int i = 1; i <= 10000; i++) {
            while (counting[i] > 0) {
                sb.append(i).append('\n');
                counting[i]--;
            }
        }
        
        // 전체 결과 출력
        System.out.print(sb.toString());
    }
}
