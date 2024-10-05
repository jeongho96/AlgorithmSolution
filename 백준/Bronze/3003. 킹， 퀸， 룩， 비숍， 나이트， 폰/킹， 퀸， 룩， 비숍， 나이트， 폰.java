

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static int[] solution(String input){
        int[] inputArray = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] result = new int[inputArray.length];
        int[] answer = {1, 1, 2, 2, 2, 8};

        for(int i = 0; i < inputArray.length; i++){
            result[i] = answer[i] - inputArray[i];
        }

        return result;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] result = solution(s);

        // 배열을 공백으로 구분된 값으로 출력
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) {
                System.out.print(" ");
            }
        }
    }
}
