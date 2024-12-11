import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesCount = new HashMap<>();

        for (String[] cloth : clothes) {
            clothesCount.put(cloth[1], clothesCount.getOrDefault(cloth[1], 0) + 1);
        }

        int answer = 1;
        for (int count : clothesCount.values()) {
            answer *= (count + 1); // 안 입는 경우 포함
        }

        return answer - 1; // 모두 안 입는 경우 제외
    }
}