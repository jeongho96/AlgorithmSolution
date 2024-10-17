class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for(int n = i; n <= j; n++){
            for(int m = 0; m < String.valueOf(n).length(); m++){
                if(String.valueOf(n).charAt(m) == String.valueOf(k).charAt(0)){
                    answer++;
                }
            }
        }

        return answer;
    }
}