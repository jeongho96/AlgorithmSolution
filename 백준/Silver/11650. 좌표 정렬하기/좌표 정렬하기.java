import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        int[][] targetArray = new int[n][2];

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            targetArray[i][0] = Integer.parseInt(st.nextToken());
            targetArray[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(targetArray, (a,b) ->{
            if(a[0] != b[0]) return a[0] - b[0];
            else return a[1] - b[1];
        });

        Arrays.stream(targetArray).forEach(a -> System.out.println(a[0] + " " + a[1]));

    }
}
