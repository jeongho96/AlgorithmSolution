import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;

        // N을 5로 계속 나누면서 몫을 더함
        while (N >= 5) {
            count += N / 5;
            N /= 5;
        }

        System.out.println(count);
    }
}
