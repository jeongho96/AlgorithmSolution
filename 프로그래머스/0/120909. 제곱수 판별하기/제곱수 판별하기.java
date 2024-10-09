import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(int n) {
        int answer = 2;
        List<Integer> list = new ArrayList<Integer>();

        for(int i = 1; i <= n; i++){
            if(n % i == 0){
                list.add(i);
            }
        }

        int sqrtNum = (int)Math.floor(Math.sqrt((double)n));

        System.out.println(sqrtNum);

        if(list.contains((int)Math.floor(Math.sqrt((double)n)))){
            answer = 1;
        }
        return answer;
    }
}