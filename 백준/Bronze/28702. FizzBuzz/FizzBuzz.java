
import java.util.Scanner;


public class Main {

    public static String solution(Integer start, Integer middle, Integer end){
        String answer = "";
        Integer number = 0;
        if(start != null){
            number = start + 3;
        }
        else if(middle != null){
            number = middle + 2;
        }
        else if(end != null){
            number = end + 1;
        }

        if(number % 3 == 0 && number % 5 == 0){
            answer = "FizzBuzz";
        }
        else if(number % 3 == 0){
            answer = "Fizz";
        }
        else if(number % 5 == 0){
            answer = "Buzz";
        }
        else{
            answer = String.valueOf(number);
        }

        return answer;
    }



    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer start = parseIntOrNull(sc.nextLine());
        Integer middle = parseIntOrNull(sc.nextLine());
        Integer end = parseIntOrNull(sc.nextLine());

        System.out.println(solution(start, middle, end));

    }

    private static Integer parseIntOrNull(String input) {
        try {
            return Integer.parseInt(input);
        } catch (NumberFormatException e) {
            return null;
        }
    }
}
