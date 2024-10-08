
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int[] solution(int[][] arr){
        // 0, 1, 2 : 최대값, 행, 열 번호
        int[] answer = new int[3];
        int maxNum = Integer.MIN_VALUE;
        int xIndex = 0;
        int yIndex = 0;

        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++){
                if(arr[i][j] > maxNum){
                    maxNum = arr[i][j];
                    xIndex = i + 1;
                    yIndex = j + 1;
                }
            }
        }
        answer[0] = maxNum;
        answer[1] = xIndex;
        answer[2] = yIndex;

        return answer;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] arr = new int[9][9];

        for(int i = 0; i < 9; i++){
            String[] line = br.readLine().split(" ");
            for(int j = 0; j < 9; j++){
                arr[i][j] = Integer.parseInt(line[j]);
            }
        }

        int[] answer = solution(arr);
        System.out.printf("%d\n%d %d", answer[0], answer[1], answer[2]);

    }
}
