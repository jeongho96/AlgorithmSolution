import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = {};
        List<Integer> tempList = new ArrayList<>();
        // 1. 반복문으로 1씩 증가해서 배열로 만들어 넣자.
        for(int i = start_num; i <= end_num; i++){
            tempList.add(i);
        }

        answer = tempList.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}