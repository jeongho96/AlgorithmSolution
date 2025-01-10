
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        String[][] personArray = new String[n][2];


        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            personArray[i][0] = st.nextToken();
            personArray[i][1] = st.nextToken();
        }

        Integer[] originalIndex = new Integer[n];
        for(int i = 0; i < n; i++) {
            originalIndex[i] = i;
        }

        Arrays.sort(originalIndex, (a,b) ->{
            if(Integer.valueOf(personArray[a][0]) != Integer.valueOf(personArray[b][0])) {
                return Integer.valueOf(personArray[a][0]) - Integer.valueOf(personArray[b][0]);
            }
            else{
                return a - b;
            }
        });
        String[][] sortedArray = new String[personArray.length][];
        for(int i = 0; i < personArray.length; i++) {
            sortedArray[i] = personArray[originalIndex[i]];
        }

        Arrays.stream(sortedArray).forEach(a -> System.out.println(a[0] + " " + a[1]));
    }
}
