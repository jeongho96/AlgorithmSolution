class Solution {
    public int solution(int order) {
        String orderString = "" + order;
        int answer = 0;

        for(char a : orderString.toCharArray()){
            if(a == '3' || a == '6' || a == '9'){
                answer += 1;
            }
        }

        return answer;
    }
}