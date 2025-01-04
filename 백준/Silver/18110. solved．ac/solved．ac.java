
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.valueOf(br.readLine());
        Integer[] scoreArray = new Integer[N];
        for (int i = 0; i < N; i++) {
            int a = Integer.valueOf(br.readLine());
            scoreArray[i] = a;
        }

        Arrays.sort(scoreArray);

        // 절사 비율 계산 (반올림)
        int cutNumber = (int) Math.round(N * 0.15);

        // 절사평균 계산
        int sum = 0;
        for (int i = cutNumber; i < N - cutNumber; i++) {
            sum += scoreArray[i];
        }

        // 평균 계산 (반올림)
        int validCount = N - 2 * cutNumber; // 절사된 항목 제외
        int result = (int) Math.round((double) sum / validCount);

        System.out.println(result);




    }


}
