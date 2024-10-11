import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {

    // 호텔 정문으로부터 가장 거리가 짧은 빈 방에 손님을 배치
    // 호텔은 W(width)개 방이 있는 H(height)층 건물
    public static String solution(int h, int w, int n) {
        // 층수 계산: (n - 1) % h + 1
        // 손님이 1부터 시작이니까 인덱스 맞춰주고(n-1) 층 수만큼 나눈 뒤
        // 나머지가 0부터 시작이니까 1 더하기.
        int floor = (n - 1) % h + 1;
        // 방 번호 계산: (n - 1) / h + 1
        int roomNumber = (n - 1) / h + 1;

        // 방 번호가 한 자리일 경우 앞에 0을 붙여 두 자리로 만들어줌
        return floor + String.format("%02d", roomNumber);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int height = input[0];
            int width = input[1];
            int number = input[2];

            System.out.println(solution(height, width, number));
        }
    }
}