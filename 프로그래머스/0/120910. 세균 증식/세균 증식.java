class Solution {
    public int solution(int n, int t) {
       int answer = n;
        for(int i = 2; i <= t+1; i++){
            answer = answer * 2;
        }
        
        return answer;
    }
}