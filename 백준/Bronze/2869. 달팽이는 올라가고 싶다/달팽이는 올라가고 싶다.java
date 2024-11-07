import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int solution(int A, int B, int V) {
        // 그냥이면 V / (A - B) 겠지만, 마지막 날에 정상 도착이므로 고려해야함.
        // 마지막 날을 제외한 V - A 거리에서 A - B에 대해 하루를 추가한게 답.
        // 올림 처리를 위해 Math.ceil을 사용하여 계산
        int days = (int) Math.ceil((double) (V - A) / (A - B)) + 1;
        return days;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 여러 값 한 줄 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        System.out.println(solution(A, B, V));
    }
}
