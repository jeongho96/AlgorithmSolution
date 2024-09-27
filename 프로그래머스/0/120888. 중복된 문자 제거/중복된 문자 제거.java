class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            char currentChar = my_string.charAt(i);

            // answer에 현재 문자가 포함되어 있는지 확인
            if (answer.toString().contains(String.valueOf(currentChar))) {
                continue;
            } else {
                answer.append(currentChar);
            }
        }


        return answer.toString();
    }
}