import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        char[] charString = my_string.toLowerCase().toCharArray();
        Arrays.sort(charString);

        return new String(charString);
    }
}