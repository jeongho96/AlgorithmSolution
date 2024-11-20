import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> playerMap = new HashMap<String, Integer>();

        for(String s : participant) {
            if(playerMap.containsKey(s)) {
                playerMap.put(s, playerMap.get(s) + 1);
            }
            else {
                playerMap.put(s, 1);
            }
        }

        for(String s : completion) {
            playerMap.put(s, playerMap.get(s) - 1);
        }

        String answer = "";
        for(String s : playerMap.keySet()) {
            if(playerMap.get(s) != 0) answer += s + "";
        }

        return answer;
    }
}