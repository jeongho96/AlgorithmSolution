import java.util.Scanner;


public class Main {

    public static int solution(int N){

        int count = 0;
        int number = 666;
        while(N != count){
            // 숫자를 문자열로 바꿨을 때 666이 포함한다면 count를 증가.
            if(String.valueOf(number).contains("666")){
                count++;

            }
            number++;

        }

        return number - 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        System.out.println(solution(N));

        sc.close();
    }
}
