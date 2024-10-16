import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.valueOf(br.readLine());
        int[] numArray = new int[n];


        for(int i = 0; i < n; i++){
            numArray[i] = Integer.valueOf(br.readLine());
        }

        Arrays.sort(numArray);

        for(int i = 0; i < numArray.length; i++){
            System.out.println(numArray[i]);
        }
    }
}
