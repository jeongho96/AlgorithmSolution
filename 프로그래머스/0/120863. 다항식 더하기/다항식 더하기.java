import java.util.Arrays;
import java.util.List;

class Solution {
    public static String solution(String polynomial){
        
        String answer = "";

        List<String> strList = List.of(polynomial.split(" "));
        int numSum = 0;
        int xSum = 0;

        for (String temp : strList) {
            if (temp.equals("+") || temp.isEmpty()) {
                continue;
            }

            if (temp.charAt(temp.length() - 1) != 'x') {
                // 숫자 항 처리
                numSum += Integer.parseInt(temp);
            } else {
                // x 항 처리 ("x"만 있는 경우와 "2x" 같은 경우 구분)
                xSum += temp.length() == 1 ? 1 : Integer.parseInt(temp.substring(0, temp.length() - 1));
            }
        }

        // x항과 숫자 항을 조합하여 정답을 생성
        if (xSum > 0) {
            if (xSum == 1) {
                answer += "x";
            } else {
                answer += xSum + "x";
            }
        }

        if (numSum > 0) {
            if (!answer.isEmpty()) {
                answer += " + ";
            }
            answer += numSum;
        }

        // numSum과 xSum 둘 다 0인 경우 처리
        if (answer.isEmpty()) {
            return "0";
        }

        return answer;

    }
}