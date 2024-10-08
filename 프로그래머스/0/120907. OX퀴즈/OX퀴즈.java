class Solution {
    public String[] solution(String[] quiz) {
                String[] answer = new String[quiz.length];
        for(int i = 0; i < quiz.length; i++){
            String[] expression = quiz[i].split(" ");
            int result = Integer.parseInt(expression[0]);
            for(int j = 1; j < expression.length; j += 2){
                String operator = expression[j];
                int number = Integer.parseInt(expression[j + 1]);


                if(operator.equals("+")){
                    result += number;
                }
                else if(operator.equals("-")){
                    result -= number;
                }
            }

            if(result == Integer.parseInt(expression[4])){
                answer[i] = "O";
            }
            else{
                answer[i] = "X";
            }

        }


        return answer;
    }
}