class Solution {
    public String solution(String my_string) {
        String answer = "";

        String upperString = my_string.toUpperCase();
        String lowerString = my_string.toLowerCase();

        for(char c : my_string.toCharArray()){
            if(upperString.contains(String.valueOf(c))){
                answer += String.valueOf(c).toLowerCase();
            }
            else if(lowerString.contains(String.valueOf(c))){
                answer += String.valueOf(c).toUpperCase();
            }
        }

        return answer;
    }
}