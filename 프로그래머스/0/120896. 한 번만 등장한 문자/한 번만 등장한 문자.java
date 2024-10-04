import java.util.Arrays;

class Solution {
    public String solution(String s) {
        int[] frequency = new int[26]; // 알파벳 소문자 a-z를 위한 배열

        // 각 문자의 빈도 계산
        for (char c : s.toCharArray()) {
            frequency[c - 'a']++;  // a의 ASCII 값에서 인덱스를 맞춤
        }

        // 한 번만 등장한 문자 추출
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (frequency[c - 'a'] == 1) {
                result.append(c);
            }
        }

        // 사전 순으로 정렬
        char[] uniqueChars = result.toString().toCharArray();
        Arrays.sort(uniqueChars);

        return new String(uniqueChars);  // 정렬된 문자열 반환
    }
}