class Solution {
    public int solution(int num, int k) {
        int answer = -1;

        String numStr = String.valueOf(num);
        char kchar = (char) (k + '0');

        for(int i = 0; i < numStr.length(); i++){
            System.out.printf("%c = %d \n",numStr.charAt(i), k);
            if((int) numStr.charAt(i) == kchar){
                answer = i + 1;
                break;
            }
        }

        return answer;
    }
}