import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int n, int[] numList) {
        List<Integer> list = new ArrayList<>();

        for(int i = 0; i < numList.length; i++){
            if(numList[i] % n == 0){
                list.add(numList[i]);
            }
        }

        return list.stream().mapToInt(i -> i).toArray();
    }
}