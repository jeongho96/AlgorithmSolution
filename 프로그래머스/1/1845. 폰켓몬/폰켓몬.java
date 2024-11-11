import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        int limitSize = nums.length / 2;

        if(map.keySet().size() <= limitSize){
            answer = map.keySet().size();
        }
        else{
            answer = limitSize;
        }

        return answer;
    }
}