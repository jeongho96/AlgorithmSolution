import java.util.stream.IntStream;

class Solution {
    public int solution(String my_string) {
        // 숫자가 아닌 경우에는 제거해서 문자열로 생성
        String numberOnly = my_string.replaceAll("[^0-9]", "");

        int[] answer = new int[numberOnly.length()];

        for(int i =0; i < numberOnly.length(); i++) {
            answer[i] = numberOnly.charAt(i) - '0';
        }

        
        int sum = IntStream.of(answer).sum();
        return sum;
    }
}