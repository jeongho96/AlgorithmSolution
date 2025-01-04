import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0; i < commands.length; i++){
            int start = commands[i][0] - 1;
            int end = commands[i][1];
            int number = commands[i][2];
            
            int[] target = Arrays.copyOfRange(array, start, end);
            Arrays.sort(target);
            answer[i] = target[number - 1];
        }
        
        
        
        return answer;
    }
}