import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // 최소공배수와 최대공약수
    // 최대공약수는 유클리드 호제법에 따라
    // GCD(a,b) = GCD(b,a, mod b)
    // lcm(a,b) = a * b / GCD(a,b)
    public static int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] targetArray = new int[2];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        targetArray[0] = Integer.parseInt(st.nextToken());
        targetArray[1] = Integer.parseInt(st.nextToken());

        System.out.println(gcd(targetArray[0], targetArray[1]));
        System.out.println(lcm(targetArray[0], targetArray[1]));
    }
}
