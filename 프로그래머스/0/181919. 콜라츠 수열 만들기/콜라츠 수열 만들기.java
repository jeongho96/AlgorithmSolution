import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<Integer>();
        list.add(n);
        for(int i = n; i > 0;){
            if(i % 2 == 0){
                i = i / 2;
                list.add(i);
            }
            else if(i % 2 != 0){
                i = 3 * i + 1;
                list.add(i);
            }

            if(i == 1 || list.size() > n){
                break;
            }
        }

        int[] answer = list.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}