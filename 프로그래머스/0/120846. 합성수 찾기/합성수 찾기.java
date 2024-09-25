class Solution {
    public int solution(int n) {
       // 1과 자기자신은 이미 포함
        int answer = 0;

        for(int i = 2; i <= n; i++) {
            int checkNumber = 0;

            for(int j = 1; j <= i; j++) {
                if(i % j == 0) {
                    checkNumber += 1;
                }
            }

            if(checkNumber > 2) answer++;

        }

        return answer;
    }
}