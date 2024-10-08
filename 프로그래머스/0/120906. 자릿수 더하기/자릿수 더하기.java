class Solution {
    public int solution(int n) {
       int answer = 0;
        String strN = String.valueOf(n);

        for(char c : strN.toCharArray()){
            answer += Integer.parseInt(String.valueOf(c));
        }

        return answer;
    }
}