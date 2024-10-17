import java.util.Scanner;


public class Main {
    public static int solution(int[] array){
        int answer = 0;

        for(int num : array){
            int checkPrimary = 0;
            if(num > 2 && num % 2 == 0) continue;
            for(int i = 1; i <= num; i++){
                if(checkPrimary > 2) break;

                if(num % i == 0) checkPrimary++;
            }

            if(checkPrimary == 2) answer++;
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] array = new int[n];

        for(int i = 0; i < n; i++){
            array[i] = sc.nextInt();
        }

        System.out.println(solution(array));
    }
}
