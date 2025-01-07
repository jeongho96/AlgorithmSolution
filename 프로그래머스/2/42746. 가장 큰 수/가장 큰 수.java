import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(int[] numbers) {
        // 숫자 배열을 문자열 배열로 변환
        String[] strNums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strNums[i] = String.valueOf(numbers[i]);
        }

        // 문자열 배열을 정렬 (커스텀 Comparator 사용)
        Arrays.sort(strNums, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                String ab = a + b;
                String ba = b + a;
                return ba.compareTo(ab); // 내림차순 정렬
            }
        });

        // 정렬 결과를 합쳐서 최종 문자열 생성
        StringBuilder result = new StringBuilder();
        for (String str : strNums) {
            result.append(str);
        }

        // 결과가 "000..."인 경우 "0" 반환
        if (result.charAt(0) == '0') {
            return "0";
        }

        return result.toString();
    }
}