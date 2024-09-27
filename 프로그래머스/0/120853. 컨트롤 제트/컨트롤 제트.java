class Solution {
    public int solution(String s) {
        String[] numberList = s.split(" ");
        int answer = 0;
        for(int i = 0; i < numberList.length; i++){



            if(numberList[i].equals("Z")){
                answer -= Integer.parseInt(numberList[i-1]);
            }
            else{
                answer += Integer.parseInt(numberList[i]);
            }
        }

        return answer;
    }
}